#!/usr/bin/env bash

set -e

# Push Docker image
docker build . --tag latest
docker tag latest registry.digitalocean.com/kevincolyar-sensors/latest
docker push registry.digitalocean.com/kevincolyar-sensors/latest

# Rollout deployment
export KUBECONFIG=./k8/k8s-1-22-8-do-1-sfo3-1653447631981-kubeconfig.yml
kubectl rollout restart deployments sensors-deploy
