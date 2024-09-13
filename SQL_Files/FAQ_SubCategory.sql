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
-- Table structure for table `FAQ_SubCategory`
--

DROP TABLE IF EXISTS `FAQ_SubCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FAQ_SubCategory` (
  `faq_category_code` varchar(10) NOT NULL,
  `faq_subcategory_id` tinyint NOT NULL AUTO_INCREMENT,
  `faq_subcategory_name` varchar(25) NOT NULL,
  PRIMARY KEY (`faq_subcategory_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FAQ_SubCategory`
--

LOCK TABLES `FAQ_SubCategory` WRITE;
/*!40000 ALTER TABLE `FAQ_SubCategory` DISABLE KEYS */;
INSERT INTO `FAQ_SubCategory` VALUES ('30001',1,'배송일반'),('30001',2,'기타'),('30001',3,'예약 배송'),('30001',4,'무탠 픽업'),('30001',5,'주문제작 배송'),('30001',6,'부티크 배송'),('30002',7,'취소/반품(환불)'),('30002',8,'교환/반품'),('30002',9,'무탠 픽업 취소/환불'),('30003',10,'혜택'),('30003',11,'고객센터'),('30003',12,'AS'),('30003',13,'기타'),('30003',14,'프로모션/이벤트'),('30003',15,'웹/앱 이용 문의'),('30003',16,'후기'),('30003',17,'무쉰사 스탠다드'),('30003',18,'부티크'),('30003',19,'무쉰사 전문관'),('30003',20,'PLUS 배송'),('30003',21,'무쉰사 테라스'),('30004',22,'기타'),('30004',23,'결제수단'),('30004',24,'주문'),('30004',25,'무쉰사페이'),('30005',26,'불량/하자'),('30005',27,'상품 문의'),('30005',28,'직매입/입점'),('30006',29,'탈퇴/기타'),('30006',30,'로그인/정보'),('30006',31,'가입/인증');
/*!40000 ALTER TABLE `FAQ_SubCategory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-13 10:57:54
