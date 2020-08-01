-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: invoice_system
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

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
-- Table structure for table `individual_invoice_details`
--

DROP TABLE IF EXISTS `individual_invoice_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `individual_invoice_details` (
  `id` int(11) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `product_price` varchar(30) DEFAULT NULL,
  `product_qty` int(11) DEFAULT NULL,
  `product_desc` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `individual_invoice_details`
--

LOCK TABLES `individual_invoice_details` WRITE;
/*!40000 ALTER TABLE `individual_invoice_details` DISABLE KEYS */;
INSERT INTO `individual_invoice_details` VALUES (1,'p1','10.0',10,NULL),(2,'p1','100.0',10,NULL),(2,'p2','110.0',15,NULL),(3,'P1','12.7',12,NULL),(4,'P1','20.0',10,NULL),(5,'P1','10.0',10,NULL),(6,'P1','20.0',10,NULL),(6,'P2','15.0',200,NULL),(7,'P3','25.0',25,NULL),(8,'p1','2.0',10,NULL),(9,'pro1','12.0',10,NULL),(9,'pro2','200.0',100,NULL),(10,'Prr ','10.0',20,NULL),(11,'p','12.0',10,NULL),(12,'P10','10.0',10,NULL),(12,'P13','25.0',70,NULL),(13,'P2q','11.0',10,NULL),(13,'kadad','50.0',60,NULL),(14,'Psome','90.0',80,NULL),(15,'Last one','50.0',70,NULL),(16,'p1','15.5',100,NULL),(16,'p2','25.75',25,NULL),(17,'P1','230.0',10,'sommme'),(17,'part','75.4',80,'soaa'),(18,'Pwjq','8.5',98,'kas o'),(18,'asd ajs','10.0',20,'lasj aid asoq k'),(19,'Pq','3.0',10,'ksksk kak '),(19,'kakdm','12.0',20,'i wanr');
/*!40000 ALTER TABLE `individual_invoice_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices` (
  `invoice_id` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(60) DEFAULT NULL,
  `total_amount` varchar(30) DEFAULT NULL,
  `timestamp` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`invoice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES (1,'Hemals','118.0','2020-07-31'),(2,'Someone','3127.0','2020-07-31'),(3,'Hemamsl','179.832','2020-08-01'),(4,'Mal','236.0','2020-08-01'),(5,'Hello','118.0','2020-08-01'),(6,'Hems','3776.0','2020-08-01'),(7,'Hemal','737.5','2020-08-01'),(8,'Hems','23.6','2020-08-01'),(9,'Client','23741.6','2020-08-01'),(10,'Client','236.0','2020-08-01'),(11,'Csom','141.6','2020-08-01'),(12,'Client','2183.0','2020-08-01'),(13,'Hemals','3669.8','2020-08-01'),(14,'Somes','8496.0','2020-08-01'),(15,'Some ones','4130.0','2020-08-01'),(16,'Some client','2588.625','2020-08-01'),(17,'New cloiejj','9831.76','2020-08-01'),(18,'Hey client','1218.94','2020-08-01'),(19,'Newss','318.6','2020-08-01'),(20,'Newss','318.6','2020-08-01');
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-01 13:21:39
