-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: projectorwhatever
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `choices`
--

DROP TABLE IF EXISTS `choices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `choices` (
  `testcode` int(11) NOT NULL,
  `studentcode` int(11) NOT NULL,
  `questioncode` int(11) NOT NULL,
  `choice` int(11) DEFAULT NULL,
  PRIMARY KEY (`studentcode`,`testcode`,`questioncode`),
  KEY `testcode` (`testcode`),
  KEY `questioncode` (`questioncode`),
  CONSTRAINT `choices_ibfk_1` FOREIGN KEY (`testcode`) REFERENCES `tests` (`testcode`),
  CONSTRAINT `choices_ibfk_2` FOREIGN KEY (`studentcode`) REFERENCES `students` (`studentcode`),
  CONSTRAINT `choices_ibfk_3` FOREIGN KEY (`questioncode`) REFERENCES `questions` (`questioncode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choices`
--

LOCK TABLES `choices` WRITE;
/*!40000 ALTER TABLE `choices` DISABLE KEYS */;
INSERT INTO `choices` VALUES (1,1,3,2),(1,1,4,2),(1,1,5,1),(2,1,6,1),(2,1,7,2),(2,1,8,3),(3,1,9,4),(3,1,10,2),(3,1,11,1),(1,2,3,4),(1,2,4,1),(1,2,5,1),(4,2,12,1),(4,2,13,1),(4,2,14,1),(5,2,1,1),(5,2,2,2),(5,2,15,1);
/*!40000 ALTER TABLE `choices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `questioncode` int(11) NOT NULL AUTO_INCREMENT,
  `question` text DEFAULT NULL,
  `optiona` text DEFAULT NULL,
  `optionb` text DEFAULT NULL,
  `optionc` text DEFAULT NULL,
  `optiond` text DEFAULT NULL,
  `correctopt` int(11) DEFAULT NULL,
  `testcode` int(11) DEFAULT NULL,
  PRIMARY KEY (`questioncode`),
  KEY `testcode` (`testcode`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`testcode`) REFERENCES `tests` (`testcode`),
  CONSTRAINT `4options` CHECK (`correctopt` in (1,2,3,4))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'The board game, Nightmare was released in what year?','1995','1992','1989','1991',4,5),(2,'Which band name isn\'t a Stand in \"JoJo\'s Bizzare Adventure\"?','Green Day','AC/DC','Survivor','Red Hot Chili Peppers',2,5),(3,'Folic acid is the synthetic form of which vitamin?','Vitamin A','Vitamin C','Vitamin B','Vitamin D',3,1),(4,'What two characters from the game Undertale are never in a relationship or not related?','Sans & Papyrus','Frisk & Chara','Alphys & Undyne','Toriel & Asgore',2,1),(5,'Which one of these rulers did not belong to the Habsburg dynasty?','Philip V','Francis Joseph','Philip II','Charles V',1,1),(6,'The manga JoJo\'s Bizarre Adventure is split into how many parts?','4a','8','6','3',2,2),(7,'When was Elvis Presley born?','July 18, 1940','January 8, 1935','December 13, 1931','April 17, 1938',2,2),(8,'In the game \"Subnautica\", which feature was removed due to performance issues in 2016?','Building','Terraforming','Multiplayer','Crafting',2,2),(9,'What is the real name of the famous spanish humorist, El Risitas?','Ernesto Guevara','Jesus Quintero','Gabriel Garcia Marquez','Juan Joya Borga',4,3),(10,'What is the surname of the character Daryl in AMC\'s show The Walking Dead?','Grimes','Dixon','Dicketson','Dickinson',2,3),(11,'Which car tire manufacturer is famous for its \"P Zero\" line?','Pirelli','Michelin','Bridgestone','Goodyear',1,3),(12,'\"Gimmick!\" is a Japanese Famicom game that uses a sound chip expansion in the cartridge. What is it called?','FME-7','VRC7','VRC6','MMC5',1,4),(13,'Which of the following colors does the Zombie eyes glow in the \"Nuketown\" map in \"Call of Duty: Black Ops II\" Zombies mode?','Blue and White','Yellow and Red','Red and Blue','Yellow and Blue',4,4),(14,'What vulnerability ranked #1 on the OWASP Top 10 in 2013?','Injection ','Cross-Site Scripting','Broken Authentication','Insecure Direct Object References',1,4),(15,'Which of these musicals won the Tony Award for Best Musical?','American Idiot','Newsies','Rent','The Color Purple',3,5);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scores` (
  `studentcode` int(11) DEFAULT NULL,
  `testcode` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
INSERT INTO `scores` VALUES (1,1,3),(1,2,0),(1,3,0),(2,1,1),(2,4,2),(2,5,1);
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `studentcode` int(11) NOT NULL,
  `name` varchar(32) DEFAULT NULL,
  `password` char(64) DEFAULT NULL,
  PRIMARY KEY (`studentcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Sade Matthews','$2a$12$WF3zfMJbMQXPlzDWaYvoae3yM/93OL8p5CeHT627qadaDRojY6Vu6'),(2,'Nabila Kaiser','$2a$12$pAGHGTe5a8JCb4yocJJxzOyKzqV2ZW6hxX.PnFpxvAzZnSWaVjsmy'),(3,'Bane Stalkinson','$2a$12$epCPN0n.UhJWqt0uzDkfLu67J.OI62TnTOF5RDQyHBp8I79eQwOfK');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subjects` (
  `subjectcode` int(11) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`subjectcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES (1,'Geography'),(2,'Entertainment'),(3,'Politics');
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tests`
--

DROP TABLE IF EXISTS `tests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tests` (
  `testcode` int(11) NOT NULL AUTO_INCREMENT,
  `subjectcode` int(11) DEFAULT NULL,
  `testname` varchar(32) DEFAULT NULL,
  `timemin` int(11) DEFAULT NULL,
  PRIMARY KEY (`testcode`),
  KEY `subjectcode` (`subjectcode`),
  CONSTRAINT `tests_ibfk_1` FOREIGN KEY (`subjectcode`) REFERENCES `subjects` (`subjectcode`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tests`
--

LOCK TABLES `tests` WRITE;
/*!40000 ALTER TABLE `tests` DISABLE KEYS */;
INSERT INTO `tests` VALUES (1,3,'Random test #1',8),(2,2,'Random test #2',14),(3,3,'Random test #3',28),(4,2,'Random test #4',12),(5,3,'Random Test #5',28);
/*!40000 ALTER TABLE `tests` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 21:28:07
