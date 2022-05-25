CREATE TABLE errors (
	id serial PRIMARY KEY,
	route VARCHAR ( 255 ) NOT NULL,
	method VARCHAR ( 50 ) NOT NULL,
	payload VARCHAR ( 255 ) NOT NULL,
	created_at timestamp without time zone default (now() at time zone 'utc')
);

CREATE TABLE measurements (
	id serial PRIMARY KEY,
	type VARCHAR ( 255 ) NOT NULL,
	device_id INTEGER NOT NULL,
	value DOUBLE PRECISION NULL,
	created_at timestamp without time zone default (now() at time zone 'utc')
);

CREATE PROCEDURE errors_insert(_route varchar, _method varchar, _payload varchar)
LANGUAGE SQL
AS $BODY$
    INSERT INTO errors(route, method, payload)
    VALUES(_route, _method, _payload);
$BODY$;

CREATE PROCEDURE measurements_insert(_type varchar, _device_id int, _value double precision, _created_at timestamp)
LANGUAGE SQL
AS $BODY$
    INSERT INTO measurements(type, device_id, value, created_at)
    VALUES(_type, _device_id, _value, _created_at);
$BODY$;
