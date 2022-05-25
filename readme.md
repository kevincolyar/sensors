# Sensors

## What to Know

    http://sensors.kevin.colyar.net/v1/

## API Documentation

    http://sensors.kevin.colyar.net/v1/docs

## Development

    http://localhost:3001/v1/docs

## Deployment

    ./bin/deploy.sh

## Testing

### Test Suite

    docker compose run api pytest
    
### Test Coverage

    docker compose exec api coverage run -m pytest
    docker compose exec api coverage report -m
    docker compose exec api coverage html

    open htmlcov/index.html
    
### Command Line

    curl -X "DELETE" http://localhost:3001/v1/errors

    curl -X POST -H "Content-Type: application/json" \
    -d '{"data": "365951380:1640995229697:'Temperature':58.48256793121914"}' \
    http://localhost:3001/v1/temp

    curl -X POST -H "Content-Type: application/json" \
    -d '{"data": "365951380:1640995229697:'Temperature':90.0"}' \
    http://localhost:3001/v1/temp

    curl -X POST -H "Content-Type: application/json" \
    -d '{"data": ":1640995229697:'Temperature':90.0"}' \
    http://localhost:3001/v1/temp

## Questions

Q: What unit is temperature?

A: Assuming fahrenheit based on example data range (e.g. 58.5 & over 90 threshold).

Q: What timezone should `formatted_time` be returned in?

A: Assuming UTC since offset not specified in given format.

## References

https://fastapi.tiangolo.com/tutorial/testing/

https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/
