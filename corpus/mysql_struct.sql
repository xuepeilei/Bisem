drop database if exists bisem;

create database bisem;

use bisem;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure
-- ----------------------------
DROP TABLE IF EXISTS `bigram`;
CREATE TABLE `bigram` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST` varchar(255) DEFAULT NULL,
  `SECOND` varchar(255) DEFAULT NULL,
  `FREQUENTNESS` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=61203 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sememe
-- ----------------------------
DROP TABLE IF EXISTS `sememe`;
CREATE TABLE `sememe` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `S` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sem_w
-- ----------------------------
DROP TABLE IF EXISTS `sem_w`;
CREATE TABLE `sem_w` (
  `SEM_ID` int(11) DEFAULT NULL,
  `SEM_W` varchar(255) DEFAULT NULL,
  KEY `SEM_ID` (`SEM_ID`),
  CONSTRAINT `SEM_ID` FOREIGN KEY (`SEM_ID`) REFERENCES `sememe` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for senses
-- ----------------------------
DROP TABLE IF EXISTS `senses`;
CREATE TABLE `senses` (
  `NO` int(11) NOT NULL,
  `W_C` varchar(255) DEFAULT NULL,
  `G_C` varchar(255) DEFAULT NULL,
  KEY `NO` (`NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sen_def
-- ----------------------------
DROP TABLE IF EXISTS `sen_def`;
CREATE TABLE `sen_def` (
  `NO_ID` int(11) NOT NULL,
  `DEF` varchar(255) DEFAULT NULL,
  KEY `NO_ID` (`NO_ID`),
  CONSTRAINT `NO_ID` FOREIGN KEY (`NO_ID`) REFERENCES `senses` (`NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sigram
-- ----------------------------
DROP TABLE IF EXISTS `sigram`;
CREATE TABLE `sigram` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST` varchar(255) DEFAULT NULL,
  `FREQUENTNESS` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17004 DEFAULT CHARSET=utf8;
