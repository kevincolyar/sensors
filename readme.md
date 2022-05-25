# Title 

## Development

## Deployment

    docker build . --tag latest
    docker tag latest registry.digitalocean.com/kevincolyar/latest 
    docker push registry.digitalocean.com/kevincolyar/latest

## Testing

    docker compose run api pytest

## Questions

Q: What unit is temperature?
A: Assuming fahrenheit based on example data range (e.g. 58.5 & over 90 threshold).

Q: What timezone should `formatted_time` be returned in?
A: Assuming UTC since offset not specified in given format.

## References

https://fastapi.tiangolo.com/tutorial/testing/
https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/
