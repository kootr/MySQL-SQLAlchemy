CREATE TABLE journey (
  id INT(11) NOT NULL AUTO_INCREMENT,
  journey_id VARCHAR(36) NOT NULL,
  client_id INT(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY journey_id (journey_id),
  KEY client_id (client_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO journey (
  id,
  journey_id,
  client_id
) VALUES (
  1,
  '9fd3fa6c-01ca-485a-a73f-edc436bbddeb',
  44
);