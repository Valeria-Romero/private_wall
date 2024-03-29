-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema private_wall_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema private_wall_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `private_wall_db` DEFAULT CHARACTER SET utf8 ;
USE `private_wall_db` ;

-- -----------------------------------------------------
-- Table `private_wall_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `private_wall_db`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message_text` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `private_wall_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
  


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


SELECT * FROM users WHERE id != 2;

SELECT * FROM messages;

INSERT INTO messages(message_text, user_id) VALUES ("Hola", 1);

INSERT INTO users(first_name, last_name, email, password) VALUES ('Max','Rodriguez','max@gmail.com', '$2b$12$MJQe0eTnYei6C0QgDCMsHOhu6En98k1oMHtwogKMXeZ/alJk88THi');

SELECT users.first_name as receiver, messages FROM users, messages LEFT JOIN messages ON users.id = messages.user_id  WHERE users.id =  1;

SELECT users.first_name, messages.* FROM users LEFT JOIN messages ON users.id = messages.user_id
