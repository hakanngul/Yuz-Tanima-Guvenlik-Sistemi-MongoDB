CREATE TABLE vardiya (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(255)
);

CREATE TABLE supervisor (
  id varchar(255),
  full_name varchar(20),
  username varchar(20),
  password varchar(20),
  email varchar(20),
  image_path varchar(255),
  phone varchar(11),
  user_role varchar(20),
  vardiya_id varchar(255)
);

ALTER TABLE vardiya ADD FOREIGN KEY (id) REFERENCES supervisor (vardiya_id);
