/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2017-04-14 17:55:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bigram
-- ----------------------------
DROP TABLE IF EXISTS `bigram`;
CREATE TABLE `bigram` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST` varchar(255) DEFAULT NULL,
  `SECOND` varchar(255) DEFAULT NULL,
  `FREQUENTNESS` int(11) DEFAULT NULL,
  `FREQUENCY` float NOT NULL,
  `MI` float unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=615 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bi_temp
-- ----------------------------
DROP TABLE IF EXISTS `bi_temp`;
CREATE TABLE `bi_temp` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `W` varchar(255) DEFAULT NULL,
  `F` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=779 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bi_words
-- ----------------------------
DROP TABLE IF EXISTS `bi_words`;
CREATE TABLE `bi_words` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `W` varchar(255) DEFAULT NULL,
  `FREQUENTNESS` int(11) DEFAULT NULL,
  `FREQUENCY` float NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=817 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sememe
-- ----------------------------
DROP TABLE IF EXISTS `sememe`;
CREATE TABLE `sememe` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `S` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8;

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
