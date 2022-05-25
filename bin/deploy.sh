#!/usr/bin/env bash

set -e

# Push Docker image
docker build . --tag latest
docker tag latest registry.digitalocean.com/kevincolyar-sensors/latest
docker push registry.digitalocean.com/kevincolyar-sensors/latest

# Rollout deployment
kubectl rollout restart deployments sensors-deploy
