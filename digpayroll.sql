-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: us-cdbr-east-06.cleardb.net    Database: heroku_dbb5a8d2e1d2fbf
-- ------------------------------------------------------
-- Server version	5.6.50-log

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

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `depID` int(11) NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(255) NOT NULL,
  PRIMARY KEY (`depID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
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
  `Localleave` int(11) DEFAULT NULL,
  `Sickleave` int(11) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (104,'AZ001','Muhammad Faarooq Azhar','Khodabux','Mr.','1993-09-30','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0','2021-11-08','20790','Front Desk Executive','ADMINISTRATION',NULL,'Monthly','100',0,0,'0','Bus','0','No','325000','13','25000','0','0','0','Bank','0','Yes',NULL,'0','22'),(84,'BG01','Gavin','Bungari','Mr.','1990-01-28','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0','2019-03-13','30900','Facilities Officer','Syndic 1CC',NULL,'Monthly','100',0,0,'1500','Car','0','No','325000','13','25000','0','0','0','Bank','1092','Yes',NULL,'0','26'),(14,'csac1','Cheong Shaow','Ah Ching','Mr.','1967-06-19','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'A190667381251E',NULL,'AFRASIA BANK, PORT LOUIS','001120700439013','25',NULL,'Paid','0',NULL,'310150','Management','Management',NULL,'Monthly','100',0,0,'5000','Car','0',NULL,'730000','13','56154','0','0','0','Bank','0','Yes',NULL,'0','26'),(15,'FONSI','Danny','Fon Sing','Mr','1968-09-15','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'F1509682807240','13056545','Mauritius Commercial Bank, Port Louis','010307850',NULL,NULL,'Paid','12000',NULL,'98500','Director','Management',NULL,'Monthly','100',22,15,'0','Car','0',NULL,'600000','13','46154','0','200000','0','Bank','0','Yes',NULL,'0','26'),(44,'LA001','Azegun','Lutchmoodoo','Mr.','0000-00-00','No','aaa','sss','ddd','7777777','88888888','fax','das@gmdd.com',NULL,'L0604793017170','18225195','Mauritius Post Cooperative Bank, Port Louis','0110002957500001',NULL,NULL,'Paid','0','0000-00-00','51792','Premises Officer','Projects Dept',NULL,'Monthly','100',22,15,'0',NULL,'0','No','435000','13','33462','0','0','32400','Bank','0','Yes',NULL,'0','26'),(13,'LEUNJ','Johnny','Leung Lam Hing','Mr.','1963-12-17','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'L171263430060E','10778126','Hong Kong Bank, Port Louis','004195277001','019899912',NULL,'Paid','10750',NULL,'185150','Management','Management',NULL,'Monthly','100',22,15,'0','Car','0','No','325000','13','25000','0','0','0','Bank','0','Yes',NULL,'162990','26'),(64,'LHHL','Laval','Law How Hung','Mr.','1963-02-16','No','aaa','aaa','aaa','7777777','88888888',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0','2017-08-02','91802','Project Development Manager','Management',NULL,'Monthly','100',0,0,'0','Car','0','No','435000','13','33462','200000','0','21000','Bank','499','Yes',NULL,'0','22'),(74,'LN001','Navish','Luchmun','Mr.','1999-12-15','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0','2022-04-21','14000','TRAINEE ENERGY AUDITOR','Projects Dept',NULL,'Monthly','100',0,0,'0','Bus','0','No','325000','13','25000','0','0','0','Bank','0','Yes',NULL,'0','22'),(94,'PA01','Prisca Angeline','Samy','Mrs.','1978-07-18','No',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0','2021-01-21','78000',' ','Management',NULL,'Monthly','100',22,15,'1000','Car','25000','No','350000','13','26923','0','0','0','Bank','0','Yes',NULL,'0','22'),(34,'PP01','Pravesh','PARBOTEEAH','Mr.','0000-00-00','No','qqq','www','eee','7777777','88888888','fax','acb@fsi.com',NULL,'P2811943028966',NULL,'The Mauritius Commercial Bank Ltd','000252837193','09',NULL,'Paid','0','0000-00-00','28920','Senior Accounting Officer','Projecs Dept',NULL,'Monthly','100',0,0,'0','Bus','0','No','325000','13','25000','0','0','0','Bank','0','Yes',NULL,'0','22');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leavedata`
--

DROP TABLE IF EXISTS `leavedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leavedata` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `Date` date DEFAULT NULL,
  `LeaveType` varchar(45) DEFAULT NULL,
  `LeaveDays` varchar(45) DEFAULT NULL,
  `ExtraLeave` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `lid_UNIQUE` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  `Month` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payable`
--

LOCK TABLES `payable` WRITE;
/*!40000 ALTER TABLE `payable` DISABLE KEYS */;
INSERT INTO `payable` VALUES (1,'csac1','310150','0','17990','0','0','0','0','0','0','0','0','1391','18609','0','0','41007','0','9305','0','213','0','730000','0','0','10652','0','329531','348140','50525','297615','0','0','0','0','0','0','0','July','2022','56154','Ah Ching July'),(3,'LEUNJ','185150','0','0','0','0','0','0','0','162990','0','0','0','0','0','0','50084','0','5555','0','213','0','325000','0','10750','25780','0','358890','348140','55852','292288','0','0','0','0','0','0','0','July','2022','25000','Leung Lam Hing July'),(4,'FONSI','98500','0','0','0','0','0','0','0','0','0','0','0','0','0','0','7344','0','2955','0','213','0','600000','0','12000','0','200000','110500','98500','10512','87988','0','0','0','0','0','0','0','July','2022','61538','Fon Sing Juky'),(44,'PP01','28920','0','0','1848','0','0','0','0','0','0','0','0','0','0','0','392','0','434','0','213','0','325000','0','0','0','0','28920','30768','1039','29729','0','0','0','0','0','0','0','July','2022','25000','PARBOTEEAH select'),(54,'LA001','51792','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2376','0','1554','0','213','0','435000','0','0','0','0','51792','51792','4143','47649','0','0','0','0','0','0','0','July','2022','35954','Lutchmoodoo July'),(64,'PP01','28920','0','0','1496','0','0','0','0','0','0','0','0','0','0','0','392','0','434','0','213','0','325000','0','0','0','0','28920','30416','1039','29377','0','0','0','0','0','0','0','August','2022','50000','PARBOTEEAH August'),(74,'LA001','51792','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2376','0','1554','0','213','0','435000','0','0','0','0','51792','51792','4143','47649','0','0','0','0','0','0','0','August','2022','71908','Lutchmoodoo August'),(84,'LA001','51792','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2376','0','1554','0','213','0','435000','0','0','0','0','51792','51792','4143','47649','0','0','0','0','0','0','0','August','2022','71908','Lutchmoodoo August');
/*!40000 ALTER TABLE `payable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paye`
--

DROP TABLE IF EXISTS `paye`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paye` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paysheet` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `EmployeeName` varchar(255) DEFAULT NULL,
  `BasicSalary` int(11) DEFAULT NULL,
  `Arrears` int(11) DEFAULT NULL,
  `Overseas` int(11) DEFAULT NULL,
  `TravelAllow` int(11) DEFAULT NULL,
  `OtherAllow` int(11) DEFAULT NULL,
  `Gross` int(11) DEFAULT NULL,
  `PAYE` int(11) DEFAULT NULL,
  `CSG` int(11) DEFAULT NULL,
  `NSF` int(11) DEFAULT NULL,
  `Medical` int(11) DEFAULT NULL,
  `SLevy` int(11) DEFAULT NULL,
  `Net` int(11) DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paysheet`
--

LOCK TABLES `paysheet` WRITE;
/*!40000 ALTER TABLE `paysheet` DISABLE KEYS */;
INSERT INTO `paysheet` VALUES (1,'csac1','Ah Ching Cheong Shaow',310150,0,20000,0,17990,348140,41007,9305,213,0,10652,286963,'August','MCPF'),(2,'FONSI','Fon Sing Danny',98500,0,5500,0,0,104000,7344,2955,213,0,0,93488,'July','Corporate Dept A'),(54,'LA001','Lutchmoodoo Azegun',51792,0,0,0,0,51792,2376,1554,213,0,0,47649,'July','Demo'),(3,'LEUNJ','Leung Lam Hing Johnny',185150,0,0,0,162990,348140,50084,5555,213,0,25780,266508,'June','Corporate Dept A'),(44,'PP01','PARBOTEEAH Pravesh',28920,0,0,0,0,28920,392,434,213,0,0,29729,'July','Demo');
/*!40000 ALTER TABLE `paysheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `EmployeeName` varchar(45) DEFAULT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `OtherDeduction` varchar(45) DEFAULT NULL,
  `Overtime` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `NSFEmpee` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `TaxableAllow` varchar(45) DEFAULT NULL,
  `Medical` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `overseas` varchar(45) DEFAULT NULL,
  `NTaxableAllow` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `AttendanceBns` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `Loan` varchar(45) DEFAULT NULL,
  `CarBenefit` varchar(45) DEFAULT NULL,
  `LeaveRef` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `SpecialBns` varchar(45) DEFAULT NULL,
  `Lateness` varchar(45) DEFAULT NULL,
  `EducationRel` varchar(45) DEFAULT NULL,
  `SpeProBns` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `MedicalRel` varchar(45) DEFAULT NULL,
  `Payable` varchar(45) DEFAULT NULL,
  `Deduction` varchar(45) DEFAULT NULL,
  `NetPay` varchar(45) DEFAULT NULL,
  `NetPaysheet` varchar(45) DEFAULT NULL,
  `CurrentGross` varchar(45) DEFAULT NULL,
  `PrevGross` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `NetCh` varchar(45) DEFAULT NULL,
  `CurrentPAYE` varchar(45) DEFAULT NULL,
  `PrevPAYE` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `eCSG` varchar(45) DEFAULT NULL,
  `eNSF` varchar(45) DEFAULT NULL,
  `eLevy` varchar(45) DEFAULT NULL,
  `Absences` varchar(45) DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1034 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (934,'AZ001','Khodabux Muhammad Faarooq Azhar','20790','0','0','1079','0','208','1100','0','0','3717','0','0','325000','0','0','0','0','0','0','0','0','0','0','0','312','0','26686','520','26166','25221','22969','0','25000','-2031','0','0','0','624','520','312','945','July','2022','AZ001 Muhammad Faarooq Azhar'),(944,'BG01','Bungari Gavin','30900','1500','0','0','0','213','0','0','1092','0','0','0','325000','0','0','0','0','0','0','0','0','0','0','0','464','0','32400','2509','29891','29891','32400','0','25000','7400','740','0','740','927','531','464','0','July','2022','BG01 Gavin'),(954,'csac1','Ah Ching Cheong Shaow','310150','5000','0','0','0','213','0','0','0','0','0','0','730000','0','0','0','0','0','0','7057','0','0','0','0','9304','0','315150','48366','266784','259727','315150','0','56154','258996','38849','0','38849','18609','531','4652','0','July','2022','csac1 Cheong Shaow'),(964,'FONSI','Fon Sing Danny','98500','0','0','0','0','213','0','0','0','0','0','0','600000','0','0','0','0','12000','0','0','0','0','200000','0','2955','0','98500','10512','87988','87988','110500','0','61538','48962','7344','0','7344','5910','531','1478','0','July','2022','FONSI Danny'),(974,'LA001','Lutchmoodoo Azegun','51792','0','0','0','0','213','0','0','0','0','0','0','435000','0','0','0','0','0','0','0','0','0','0','0','1554','32400','51792','4143','47649','47649','51792','0','35954','15838','2376','0','2376','3108','531','777','0','July','2022','LA001 Azegun'),(984,'LEUNJ','Leung Lam Hing Johnny','185150','0','0','0','0','213','0','0','0','0','0','0','325000','0','0','0','0','10750','0','25780','0','0','0','162990','5554','0','348140','55851','292289','266509','358890','0','25000','333890','50084','0','50084','11109','531','2777','0','July','2022','LEUNJ Johnny'),(994,'LHHL','Law How Hung Laval','91802','0','0','0','0','213','0','0','499','0','0','0','435000','0','0','0','0','0','0','0','0','0','0','0','2754','21000','91802','11975','79827','79827','91802','0','35077','56725','8509','0','8509','5508','531','1377','0','July','2022','LHHL Laval'),(1004,'LN001','Luchmun Navish','14000','0','0','0','0','140','0','0','0','0','0','0','325000','0','0','0','0','0','0','0','0','0','0','0','210','0','14000','350','13650','13650','14000','0','25000','-11000','0','0','0','420','350','210','0','July','2022','LN001 Navish'),(1014,'PA01','Samy Prisca Angeline','78000','1000','0','0','0','213','0','0','0','25000','0','0','350000','0','0','0','0','0','0','0','0','0','0','0','2340','0','104000','14115','89885','89885','104000','0','26923','77077','11562','0','11562','4680','531','1170','0','July','2022','PA01 Prisca Angeline'),(1024,'PP01','PARBOTEEAH Pravesh','28920','0','0','0','0','213','0','0','0','0','0','0','325000','0','0','0','0','0','0','0','0','0','0','0','434','0','28920','1039','27881','27881','28920','0','25000','3920','392','0','392','868','531','434','0','July','2022','PP01 Pravesh');
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

-- Dump completed on 2022-09-23 10:15:14
