-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: CU_Trees_Test_DB
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `TREE`
--

DROP TABLE IF EXISTS `TREE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TREE` (
  `Tnum` char(5) COLLATE latin1_bin NOT NULL,
  `Snum` int(11) NOT NULL,
  `TDate` date NOT NULL,
  PRIMARY KEY (`Tnum`,`Snum`),
  KEY `fk_TREE_TREE_TAXONOMY1_idx` (`Snum`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TREE_INFO`
--

DROP TABLE IF EXISTS `TREE_INFO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TREE_INFO` (
  `TI_Tnum` char(5) NOT NULL,
  `TI_Age` decimal(8,4) NOT NULL,
  `TI_DBH` decimal(8,4) NOT NULL,
  `TI_Height` decimal(8,4) NOT NULL,
  `TI_DoB` date DEFAULT NULL,
  `TI_DoD` date DEFAULT NULL,
  PRIMARY KEY (`TI_Tnum`),
  CONSTRAINT `TREE_INFO_ibfk_1` FOREIGN KEY (`TI_Tnum`) REFERENCES `TREE` (`Tnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TREE_LOCATION`
--

DROP TABLE IF EXISTS `TREE_LOCATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TREE_LOCATION` (
  `TL_Tnum` char(5) NOT NULL,
  `TL_LAT` decimal(8,4) NOT NULL,
  `TL_LNG` decimal(8,4) NOT NULL,
  `TL_Gnum` char(2) NOT NULL,
  PRIMARY KEY (`TL_Tnum`),
  CONSTRAINT `TREE_LOCATION_ibfk_1` FOREIGN KEY (`TL_Tnum`) REFERENCES `TREE` (`Tnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TREE_TAXONOMY`
--

DROP TABLE IF EXISTS `TREE_TAXONOMY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TREE_TAXONOMY` (
  `TT_Snum` char(5) NOT NULL,
  `TT_Cname` varchar(15) NOT NULL,
  `TT_Family` varchar(15) NOT NULL,
  `TT_Genus` varchar(15) NOT NULL,
  `TT_Specific_Epithet` varchar(15) NOT NULL,
  PRIMARY KEY (`TT_Snum`),
  UNIQUE KEY `TT_Snum` (`TT_Snum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TREE_USER`
--

DROP TABLE IF EXISTS `TREE_USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TREE_USER` (
  `TU_Tnum` char(5) NOT NULL,
  `TU_IDnum` char(5) NOT NULL,
  `TU_Lname` varchar(10) NOT NULL,
  `TU_Fname` varchar(10) NOT NULL,
  PRIMARY KEY (`TU_Tnum`),
  CONSTRAINT `TREE_USER_ibfk_1` FOREIGN KEY (`TU_Tnum`) REFERENCES `TREE` (`Tnum`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-19 10:26:57
