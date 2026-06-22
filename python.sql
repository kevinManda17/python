DROP DATABASE IF EXISTS `list`;
CREATE DATABASE IF NOT EXISTS `list`;
USE `list`

CREATE TABLE IF NOT EXISTS `fam`
(
    `id_list` int not null auto_increment ,
    `first_name` varchar(32) not null unique ,
    `last_name` varchar(32) not null,
    `age` int not null ,

    primary key(`id_list`)
);

INSERT INTO `fam`(`first_name`,`last_name`,`age`)
VALUES 
('kevin', 'manda' , 21),
('keren', 'manda', 20),
('kestia', 'manda' , 17 ),
('patricia', 'manda', 14),
('davina', 'manda ', 11),
('andrea', 'manda', 6);
