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
- [ ] Testing
- [ ] Testing - Unit tests
- [ ] Testing - REST client
- [ ] Testing - Bad type conversion

## v0.6.x
- [ ] Persistence - schema
- [ ] Persistence - indices
- [ ] Persistence - measurements
    + t
    + measurement/type
    + device_id 
    + value 
- [ ] Persistence - errors
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

## v1.1.x - Measurement persistance
- [ ] Tagged/Doc store?

## v1.2.x - Measurement persistance
- [ ] API versioning
    https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-8-project-structure-api-versioning/

## v1.2.x
- [ ] Lets Encrypt
- [ ] Kafka
