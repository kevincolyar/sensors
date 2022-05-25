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
- [X] Deployment - dns - sensors.kevin.colyar.net

## v0.4.x
- [X] POST temp
- [X] Parse data
- [X] Response - {'overtemp': False}
- [X] Response - Error handling - Overtemp
- [X] Response - Error handling
- [X] Response - Format timestamp
- [ ] Validation - device id - int32
- [ ] Validation - epoch_ms - int64
- [ ] Validation - temperature - float64
- [ ] Validation - temperature - negative

## v0.5.x
- [X] Testing - Setup
- [X] Testing - Unit tests
- [X] Testing - REST client
- [ ] Testing - Bad type conversions

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

## v0.6.x
- [ ] Documentation
https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/
- [ ] Documentation
- [ ] Documentation - API
  + https://fastapi.tiangolo.com/deployment/docker/#interactive-api-docs

## v1.1.x
- [ ] Linting
- [ ] Coverage

## v1.1.x
- [ ] Tagged/Doc store?

## v1.2.x
- [ ] API versioning
    https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-8-project-structure-api-versioning/

## v1.2.x
- [ ] Lets Encrypt
- [ ] Kafka

## v1.3.x
- [ ] Persistence - test/staging db
- [ ] Persistence - indices
- [ ] Persistence - measurements - upsert
- [ ] Persistence - errors - save stack trace
