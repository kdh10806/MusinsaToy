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
-- Table structure for table `Standard_Code`
--

DROP TABLE IF EXISTS `Standard_Code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Standard_Code` (
  `standard_code_type_id` varchar(10) NOT NULL,
  `standard_code` varchar(5) NOT NULL,
  `standard_code_type_name` varchar(15) NOT NULL,
  `standard_code_name` varchar(15) NOT NULL,
  `sort_order` smallint NOT NULL,
  `is_use` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Standard_Code`
--

LOCK TABLES `Standard_Code` WRITE;
/*!40000 ALTER TABLE `Standard_Code` DISABLE KEYS */;
INSERT INTO `Standard_Code` VALUES ('0','100','코드목차','고객문의대분류',1,'Y'),('0','200','코드목차','고객문의처리상태',2,'Y'),('0','300','코드목차','고객문의대분류',3,'Y'),('0','400','코드목차','고객문의대분류',4,'Y'),('0','500','코드목차','고객문의대분류',5,'Y'),('100','01','고객문의대분류','배송',1,'Y'),('100','02','고객문의대분류','주문/결제',2,'Y'),('100','03','고객문의대분류','취소/교환/환불',3,'Y'),('100','04','고객문의대분류','회원정보',4,'Y'),('100','05','고객문의대분류','상품확인',5,'Y'),('100','06','고객문의대분류','서비스',6,'Y'),('200','01','고객문의처리상태','답변대기',1,'Y'),('200','02','고객문의처리상태','접수',2,'Y'),('200','03','고객문의처리상태','업체문의중',3,'Y'),('200','04','고객문의처리상태','물품도착확인',4,'Y'),('200','05','고객문의처리상태','교환 상품 발송',5,'Y'),('200','06','고객문의처리상태','답변완료',6,'Y'),('300','01','FAQ대분류','배송',1,'Y'),('300','02','FAQ대분류','교환/취소(반품)',2,'Y'),('300','03','FAQ대분류','서비스',3,'Y'),('300','04','FAQ대분류','주문/결제',4,'Y'),('300','05','FAQ대분류','상품확인',5,'Y'),('300','06','FAQ대분류','회원정보',6,'Y');
/*!40000 ALTER TABLE `Standard_Code` ENABLE KEYS */;
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
