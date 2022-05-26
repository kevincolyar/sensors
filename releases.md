# Releases

## v0.1.0 - Setup
- [X] Git
- [X] Python
- [X] Docker
- [X] Documentation
- [X] Testing
- [X] Logging

## v0.2.0 - Routes
- [X] Routes - POST /temp
- [X] Routes - GET /errors
- [X] Routes - DELETE /errors

## v0.3.x - Deployment
- [X] Deployment - k8
- [X] Deployment - digitalocean
- [X] Deployment - update pods after image push
  + https://stackoverflow.com/questions/33112789/how-do-i-force-kubernetes-to-re-pull-an-image
  + kubectl rollout restart deployments sensors-deploy
- [X] Deployment - dns - sensors.kevin.colyar.net

## v0.4.x
- [X] POST temp
- [X] Parse data
- [X] Response - {'overtemp': False}
- [X] Response - Error handling - Overtemp
- [X] Response - Error handling
- [X] Response - Format timestamp
- [X] Validation - device id - int32
- [X] Validation - epoch_ms - int64
- [X] Validation - temperature - float64

## v0.5.x
- [X] Testing - Setup
- [X] Testing - Unit tests
- [X] Testing - REST client
- [X] Testing - Bad type conversions
- [X] Testing - payload larger than VARCHAR 255

## v0.6.x
- [X] Persistence - schema
- [X] Persistence - stored procedures
- [X] Persistence - measurements
    + created_at
    + measurement/type
    + device_id 
    + value 
- [X] Persistence - errors
    + timestamp
    + route
    + method
    + payload
    + sort by timestamp

## v0.7.x
- [X] Documentation
  + https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/
- [X] Documentation - API
  + https://fastapi.tiangolo.com/deployment/docker/#interactive-api-docs

## v0.8.x
- [X] API versioning

## v1.0.0
- [X] Push to github
- [X] Make github project public
- [X] Archive project
- [X] Email project

## v1.1.x
- [X] Linting
- [X] Coverage

## v1.2.x
- [ ] Persistence - test/staging db
- [ ] Persistence - indices
- [ ] Persistence - measurements - upsert
- [ ] Persistence - errors - save stack trace
- [ ] Persistence - handle db re/connection issues

## v1.3.x
- [ ] Lets Encrypt
- [ ] Kafka
- [ ] Authentication - JWT
