-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (arm64)
--
-- Host: 127.0.0.1    Database: testingdb
-- ------------------------------------------------------
-- Server version	8.0.38

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member_info`
--

DROP TABLE IF EXISTS `member_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_info` (
  `member_number` int NOT NULL AUTO_INCREMENT,
  `member_state_code` varchar(50) NOT NULL,
  `id` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL,
  `name` varchar(50) NOT NULL,
  `birth` date NOT NULL,
  `sex` varchar(1) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `login_datetime` datetime DEFAULT NULL,
  `modify_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
  `register_datetime` datetime NOT NULL,
  `exit_datetime` datetime NOT NULL DEFAULT '9999-12-31 23:59:59',
  `recommand_id` varchar(50) DEFAULT NULL,
  `login_count` tinyint NOT NULL DEFAULT '0',
  `is_admin` varchar(1) NOT NULL DEFAULT 'U',
  `note` text,
  PRIMARY KEY (`member_number`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_info`
--

LOCK TABLES `member_info` WRITE;
/*!40000 ALTER TABLE `member_info` DISABLE KEYS */;
INSERT INTO `member_info` VALUES (1,'40001','asdf1234','asdf1234!','김진철','2000-08-22','M','01012345678','asdf@naver.com','2024-08-30 12:26:32','2024-08-30 17:21:36','2023-02-20 08:09:45','9999-12-31 23:59:59',NULL,0,'U',NULL),(2,'40001','qwer1234','qwer1234!','우소미','1999-09-22','F','01009876543','qwer@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-04-21 08:09:35','9999-12-31 23:59:59','asdf1234',0,'U',NULL),(3,'40001','zxcv1234','zxcv1234!','조시형','1993-03-21','F','01023456789','zxcv@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-05-03 16:04:00','9999-12-31 23:59:59',NULL,0,'U',NULL),(4,'40002','qwerty1234','qwerty1234!','임미정','1992-05-17','F','01034567890','qwerty@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-05-17 17:08:29','9999-12-31 23:59:59',NULL,0,'U',NULL),(5,'40001','asdfgh1234','asdfgh1234!','공경민','2000-02-20','M','01045678901','asdfgh@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-06-25 08:00:00','9999-12-31 23:59:59',NULL,0,'U',NULL),(6,'40001','zxcvbn1234','zxcvbn1234!','장우원','1996-08-24','M','01056789012','zxcvbn@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-07-09 14:23:45','9999-12-31 23:59:59','asdf1234',0,'U',NULL),(7,'40001','poiu1234','poiu1234!','남라미','2001-05-04','F','01067890123','poiu@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-08-09 13:45:23','9999-12-31 23:59:59',NULL,0,'U',NULL),(8,'40001','lkjh1234','lkjh1234!','최서윤','2001-07-25','F','01078901234','lkjh@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-09-21 16:24:17','9999-12-31 23:59:59',NULL,0,'U',NULL),(9,'40004','mnbv1234','mnbv1234!','홍재안','1995-04-14','M','01089012345','mnbv@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-10-09 21:04:21','2024-08-06 15:03:47',NULL,0,'U',NULL),(10,'40001','ghjkl1234','ghjkl1234!','이정헌','1990-02-10','M','01090123456','ghjkl@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2023-11-12 08:34:23','9999-12-31 23:59:59',NULL,0,'U',NULL),(11,'40001','20230101001','20230101001!','문연지','1992-11-24','F','01001234567','yeonji@naver.com','2024-08-30 12:26:32','2024-08-30 20:39:06','2023-12-01 08:00:00','9999-12-31 23:59:59',NULL,0,'A',NULL),(12,'40001','20240101001','20240101001!','이아윤','1994-11-14','F','01087654321','ayoon@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2024-01-01 08:00:00','9999-12-31 23:59:59',NULL,0,'B',NULL),(13,'40001','20240101002','20240101002!','윤모석','1997-04-17','M','01076543210','yoon@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2024-01-01 08:00:00','9999-12-31 23:59:59',NULL,0,'B',NULL),(14,'40001','20240101003','20240101003!','오민승','2002-09-28','F','01065432109','ohmin@naver.com','2024-08-30 12:26:32','2024-08-30 12:26:32','2024-01-01 08:00:00','9999-12-31 23:59:59',NULL,0,'B',NULL),(30,'40001','kdh10806','kdh10806!','김대현','1994-01-16','M','01001234567','kdh10806@naver.com','2024-08-30 21:29:46','2024-09-12 20:07:35','2023-12-01 08:00:00','9999-12-31 23:59:59',NULL,0,'A',NULL);
/*!40000 ALTER TABLE `member_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-13 11:42:57
