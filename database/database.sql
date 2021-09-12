CREATE TABLE users (
    id                          SERIAL PRIMARY KEY,
    username                    VARCHAR(20) NOT NULL,
    credential                  VARCHAR(50) NOT NULL,
    created_at                  TIMESTAMP NOT NULL DEFAULT(now())
);