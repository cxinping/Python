create database mytestdb character set utf8 ;

use mytestdb;

DROP TABLE IF EXISTS `mytestdb`;
CREATE TABLE `employee` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
