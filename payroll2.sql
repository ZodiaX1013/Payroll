-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: payroll
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `department`
--

use heroku_dbb5a8d2e1d2fbf;

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `depID` int NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(255) NOT NULL,
  PRIMARY KEY (`depID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `eid` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Title` varchar(45) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `clocked` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `fax` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  `NICno` varchar(45) DEFAULT NULL,
  `TaxAC` varchar(45) DEFAULT NULL,
  `Bank` varchar(255) DEFAULT NULL,
  `BankAC` varchar(45) DEFAULT NULL,
  `Bankcode` varchar(45) DEFAULT NULL,
  `report` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `Carbenefit` varchar(45) DEFAULT NULL,
  `hire` date DEFAULT NULL,
  `salary` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  `Subdepartment` varchar(45) DEFAULT NULL,
  `Payescheme` varchar(45) DEFAULT NULL,
  `Payepercentage` varchar(45) DEFAULT NULL,
  `Localleave` int DEFAULT NULL,
  `Sickleave` int DEFAULT NULL,
  `Fixedallow` varchar(45) DEFAULT NULL,
  `Travelmode` varchar(45) DEFAULT NULL,
  `Travelallow` varchar(45) DEFAULT NULL,
  `expatriate` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `months` varchar(45) DEFAULT NULL,
  `MonthlyEDF` varchar(45) DEFAULT NULL,
  `Houseinterest` varchar(45) DEFAULT NULL,
  `Educationrel` varchar(45) DEFAULT NULL,
  `Medicalrel` varchar(45) DEFAULT NULL,
  `Paymentmode` varchar(45) DEFAULT NULL,
  `medical` varchar(45) DEFAULT NULL,
  `working` varchar(45) DEFAULT NULL,
  `Lastwork` date DEFAULT NULL,
  `Specialbonus` varchar(45) DEFAULT NULL,
  `Workingdays` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`eid`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `Bank AC_UNIQUE` (`BankAC`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (3,'A001','abc','xyz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'A002','pqr','def',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'A003','qwe','rty',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1,'AB001','Aniket ','Gamit','','2000-09-10','No','adajan','surat','India','77777777','77777777','abc','gamitjaydeep18@gmail.com','IMG_0204.JPG','1111','2222','','111','222','Jaydeep','','1000','2022-07-01','80000','Manager','Front-end','HTML','','100',24,24,'15000','','5000','Expatriate','1200000','12','100000','5000','10000','200000','','100000','','2022-07-31','10000','24'),(2,'AB002','Jaydeep','Gamit','Mr.','2000-09-10','No','ONGC','SURAT','India','9999999999','9999999999','abcd','gamitjaydeep18@gmail.com','x3qz52xv1cn3dvmzjtcp','1234','5678','The Hongkong and Shanghai Banking Corporation Limited','1111','1111','','Paid','1000','2022-07-01','12000','Developer','dep2','dep2','Monthly','100',24,24,'1000','','5000',NULL,'240000','12','20000','2000','4000','6000','Bank','8000','Yes',NULL,'3000','24'),(18,'AB003','xyz','abc','Mr.','2002-02-05','No','qqq','www','eee','7777777','88888888','rrr','acb@dmail.com','5p3txdpqe2stl36xgffb','0000','0000','The Hongkong and Shanghai Banking Corporation Limited','0000','0000','','Paid','0','2022-05-01','12000','dev','dep2','dep2','Yearly','100',24,24,'0','Bus','0','Expatriate','325000','13','25000','0','0','0','Bank','0','Yes',NULL,'0','24'),(6,'B001','asd','fgh',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,'B002','zxc','vbn',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,'C001','qet','wry',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,'C002','adg','sfh',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,'C003','zcb','xvn',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(14,'csac1','Cheong Shaow','Ah Ching','Mr.','1967-06-19','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'A190667381251E',NULL,'AFRASIA BANK, PORT LOUIS','001120700439013','25',NULL,'Paid','0',NULL,'310150','Management','Management',NULL,'Monthly','100',0,0,'5000','Car','0',NULL,'730000','13','56154','0','0','0','Bank','0','Yes',NULL,'0','26'),(11,'D001','qaz','wsx',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12,'D002','edc','rfv',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(15,'FONSI','Danny','Fon Sing','Mr','1968-09-15','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'F1509682807240','13056545','Mauritius Commercial Bank, Port Louis','010307850',NULL,NULL,'Paid','12000',NULL,'98500','Director','Management',NULL,'Monthly','100',22,15,'0','Car','0',NULL,'600000','13','46154','0','200000','0','Bank','0','Yes',NULL,'0','26'),(13,'LEUNJ','Johnny','Leung Lam Hing','Mr.','1963-12-17','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'L171263430060E','10778126','Hong Kong Bank, Port Louis','004195277001','019899912',NULL,'Paid','10750',NULL,'185150',NULL,'Management',NULL,'Monthly','100',22,15,'0','Car','0','No','325000','13','25000','0','0','0','Bank','0','Yes',NULL,'162990','26'),(19,'Z001','zad','zod','Mr.','2000-09-10','No','side','way','here','7777777','88888888','fax','abc@mail.com','asdbcg65hd64hd57h85g','1111','2222','MauBank Ltd','1230','1231','  ','No','0','2022-05-01','12000','Dev','dep1','sdep1','Yearly','100',24,24,'0','Car','0','Yes','325000','13','25000','0','0','0','Bank','0','Yes','2000-09-10','0','24'),(20,'Z002','zad1','zod1','Mrs.','2002-06-19','No','side','way','here','7777777','88888888','fax','abc1@mail.com','asdbcg65hd64hd5gvhd6','1111','2222','MauBank Ltd','1231','1231','Jaydeep','Yes','0','2022-07-01','15000','Test','dep2','sdep22','Yearly','100',24,24,'0','Car','0','No','325000','13','25000','0','0','0','Bank','0','Yes','2000-09-10','0','24'),(21,'Z003','zad2','zod2','Ms.','2001-02-22','Yes','side','way','here','7777777','88888888','fax','abc2@mail.com','asdbcg65hd64hd5hvg5s','1111','2222','MauBank Ltd','1232','1231','Jaydeep','Yes','0','2022-06-01','15000','Test','dep2','sdep21','Yearly','100',24,24,'0','Car','0','No','325000','13','25000','0','0','0','Bank','0','No','2022-08-30','0','24');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leavedata`
--

DROP TABLE IF EXISTS `leavedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `leavedata` (
  `lid` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `Date` date DEFAULT NULL,
  `LeaveType` varchar(45) DEFAULT NULL,
  `LeaveDays` varchar(45) DEFAULT NULL,
  `ExtraLeave` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `lid_UNIQUE` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leavedata`
--

LOCK TABLES `leavedata` WRITE;
/*!40000 ALTER TABLE `leavedata` DISABLE KEYS */;
/*!40000 ALTER TABLE `leavedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payable`
--

DROP TABLE IF EXISTS `payable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `payable` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `Overtime` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `LeaveRef` varchar(45) DEFAULT NULL,
  `SpeBonus` varchar(45) DEFAULT NULL,
  `SpeProBonus` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `TaxAllow` varchar(45) DEFAULT NULL,
  `NTaxAllow` varchar(45) DEFAULT NULL,
  `AttBonus` varchar(45) DEFAULT NULL,
  `Loan` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `Lateness` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `OtherDed` varchar(45) DEFAULT NULL,
  `NSF` varchar(45) DEFAULT NULL,
  `Medical` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `travel` varchar(45) DEFAULT NULL,
  `car` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `EducationRelief` varchar(45) DEFAULT NULL,
  `gross` varchar(45) DEFAULT NULL,
  `Payable` varchar(45) DEFAULT NULL,
  `Deduction` varchar(45) DEFAULT NULL,
  `NetPay` varchar(45) DEFAULT NULL,
  `OT1hr` varchar(45) DEFAULT NULL,
  `OT1amt` varchar(45) DEFAULT NULL,
  `OT2hr` varchar(45) DEFAULT NULL,
  `OT2amt` varchar(45) DEFAULT NULL,
  `OT3hr` varchar(45) DEFAULT NULL,
  `OT3amt` varchar(45) DEFAULT NULL,
  `LatenessHr` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payable`
--

LOCK TABLES `payable` WRITE;
/*!40000 ALTER TABLE `payable` DISABLE KEYS */;
INSERT INTO `payable` VALUES (1,'csac1','310150','0','17990','0','0','0','0','0','0','0','0','1391','18609','0','0','41007','0','9305','0','213','0','730000','0','0','10652','0','348140','348140','50525','286963','0','0','0','0','0','0','0'),(3,'LEUNJ','185150','0','162990','0','0','0','0','0','0','0','0','0','0','0','0','50084','0','5555','0','213','0','325000','0','10750','25780','0','348140','348140','55852','266508','0','0','0','0','0','0','0');
/*!40000 ALTER TABLE `payable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paye`
--

DROP TABLE IF EXISTS `paye`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `paye` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `overtime` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `LeaveRefund` varchar(45) DEFAULT NULL,
  `SpecialBonus` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `TaxableAllow` varchar(45) DEFAULT NULL,
  `SpeProBonus` varchar(45) DEFAULT NULL,
  `AttBonus` varchar(45) DEFAULT NULL,
  `CarBenefit` varchar(45) DEFAULT NULL,
  `CurrGross` varchar(45) DEFAULT NULL,
  `PrevGross` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `NetCh` varchar(45) DEFAULT NULL,
  `CurrPAYE` varchar(45) DEFAULT NULL,
  `PrevPAYE` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `pid_UNIQUE` (`pid`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paye`
--

LOCK TABLES `paye` WRITE;
/*!40000 ALTER TABLE `paye` DISABLE KEYS */;
/*!40000 ALTER TABLE `paye` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paysheet`
--

DROP TABLE IF EXISTS `paysheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `paysheet` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `EmployeeName` varchar(255) DEFAULT NULL,
  `BasicSalary` int DEFAULT NULL,
  `Arrears` int DEFAULT NULL,
  `Overseas` int DEFAULT NULL,
  `TravelAllow` int DEFAULT NULL,
  `OtherAllow` int DEFAULT NULL,
  `Gross` int DEFAULT NULL,
  `PAYE` int DEFAULT NULL,
  `CSG` int DEFAULT NULL,
  `NSF` int DEFAULT NULL,
  `Medical` int DEFAULT NULL,
  `SLevy` int DEFAULT NULL,
  `Net` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paysheet`
--

LOCK TABLES `paysheet` WRITE;
/*!40000 ALTER TABLE `paysheet` DISABLE KEYS */;
INSERT INTO `paysheet` VALUES (1,'csac1','Ah Ching Cheong Shaow',310150,0,20000,0,17990,348140,41007,9305,213,0,10652,286963,'2022-08-10','MCPF'),(2,'FONSI','Fon Sing Danny',98500,0,5500,0,0,104000,7344,2955,213,0,0,93488,'2022-07-10','Corporate Dept A'),(3,'LEUNJ','Leung Lam Hing Johnny',185150,0,0,0,162990,348140,50084,5555,213,0,25780,266508,'2022-06-10','Corporate Dept A');
/*!40000 ALTER TABLE `paysheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `salary` (
  `sid` int NOT NULL AUTO_INCREMENT,
  `Employee ID` varchar(45) NOT NULL,
  `arrears` varchar(45) DEFAULT NULL,
  `transport` varchar(45) DEFAULT NULL,
  `Other allow` varchar(45) DEFAULT NULL,
  `Local refund` varchar(45) DEFAULT NULL,
  `Sick refund` varchar(45) DEFAULT NULL,
  `Special bonus` varchar(45) DEFAULT NULL,
  `Fixed allow` varchar(45) DEFAULT NULL,
  `Disct bonus` varchar(45) DEFAULT NULL,
  `Other ded` varchar(45) DEFAULT NULL,
  `Att bonus` varchar(45) DEFAULT NULL,
  `OT1 hour` varchar(45) DEFAULT NULL,
  `OT1 amo` varchar(45) DEFAULT NULL,
  `OT2 hour` varchar(45) DEFAULT NULL,
  `OT2 amo` varchar(45) DEFAULT NULL,
  `OT3 hour` varchar(45) DEFAULT NULL,
  `OT3 amo` varchar(45) DEFAULT NULL,
  `Late hour` varchar(45) DEFAULT NULL,
  `Late amo` varchar(45) DEFAULT NULL,
  `Tax allow desc` varchar(45) DEFAULT NULL,
  `Tax allow amo` varchar(45) DEFAULT NULL,
  `NTax allow desc` varchar(45) DEFAULT NULL,
  `NTax allow amo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Employee ID`),
  UNIQUE KEY `sid_UNIQUE` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-13 13:22:24
