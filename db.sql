-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: photowallDB
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.12.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add migration history',8,'add_migrationhistory'),(23,'Can change migration history',8,'change_migrationhistory'),(24,'Can delete migration history',8,'delete_migrationhistory'),(25,'Can add web site user',9,'add_websiteuser'),(26,'Can change web site user',9,'change_websiteuser'),(27,'Can delete web site user',9,'delete_websiteuser'),(28,'Can add picture label',10,'add_picturelabel'),(29,'Can change picture label',10,'change_picturelabel'),(30,'Can delete picture label',10,'delete_picturelabel'),(31,'Can add picture',11,'add_picture'),(32,'Can change picture',11,'change_picture'),(33,'Can delete picture',11,'delete_picture'),(34,'Can add picture comment',12,'add_picturecomment'),(35,'Can change picture comment',12,'change_picturecomment'),(36,'Can delete picture comment',12,'delete_picturecomment'),(37,'Can add photo wall',13,'add_photowall'),(38,'Can change photo wall',13,'change_photowall'),(39,'Can delete photo wall',13,'delete_photowall'),(40,'Can add photo information',14,'add_photoinformation'),(41,'Can change photo information',14,'change_photoinformation'),(42,'Can delete photo information',14,'delete_photoinformation'),(43,'Can add ask for friend message',15,'add_askforfriendmessage'),(44,'Can change ask for friend message',15,'change_askforfriendmessage'),(45,'Can delete ask for friend message',15,'delete_askforfriendmessage'),(46,'Can add photowall comment',16,'add_photowallcomment'),(47,'Can change photowall comment',16,'change_photowallcomment'),(48,'Can delete photowall comment',16,'delete_photowallcomment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$DJY8lcqpO7Eb$6OFjEVth0sq8+OtPtP+rN/fXOrrLk4lz8bf5wHzLwdE=','2014-07-23 02:19:34',1,'root','','','',1,1,'2014-07-17 04:30:27'),(4,'pbkdf2_sha256$12000$Vgmh2nlcvWjc$EPY9w+op1WoI/OzoqYRx8DHMI3FegmTgruKI6ixNybE=','2014-07-23 04:48:04',0,'userss','','','a@b.c',0,1,'2014-07-18 07:22:45'),(5,'pbkdf2_sha256$12000$OUOo9gSfgBqA$n/S1Y7w3DlNCs1RJjPNA7LGPAzn+KD/xHTbdNqCK+tc=','2014-07-23 02:15:07',0,'范冰冰','','','b@c.d',0,1,'2014-07-18 07:56:30'),(6,'pbkdf2_sha256$12000$g72zumMVFrvA$q1z7Y+YK5iopcyKnSQCDIxQRW0A5HJxYwsJblE+pM74=','2014-07-20 14:06:23',0,'test','','','a@b.d',0,1,'2014-07-18 09:19:40'),(7,'pbkdf2_sha256$12000$XDvxUx73tyUo$75S8qC1DTgM9zA6BNNVkoPG3lZSJr+S3/mcScZJ22RI=','2014-07-20 14:05:17',0,'heh','','','b@c.c',0,1,'2014-07-20 14:05:17'),(8,'pbkdf2_sha256$12000$k0RIsE1skYAe$6qvhlDevR0gEB17CFGrkhJFrg4PqBKIorCH3gKkZULc=','2014-07-23 00:50:30',0,'2','','','d@a.b',0,1,'2014-07-23 00:50:30');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-07-18 07:22:14',1,3,'2','1',3,''),(2,'2014-07-18 07:22:14',1,3,'3','范冰冰',3,''),(3,'2014-07-20 13:10:19',1,15,'1','userss to test',3,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'migration history','south','migrationhistory'),(9,'web site user','picwall','websiteuser'),(10,'picture label','picwall','picturelabel'),(11,'picture','picwall','picture'),(12,'picture comment','picwall','picturecomment'),(13,'photo wall','picwall','photowall'),(14,'photo information','picwall','photoinformation'),(15,'ask for friend message','picwall','askforfriendmessage'),(16,'photowall comment','picwall','photowallcomment');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0gal6il22pv7ry0xk0q8nufaqwatr3uy','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-05 14:27:22'),('5yrui40qbkesbazj5na74rxbcyv0b9an','NTcxMDYxMWViOWJiNGQzNDIxMTE1Nzc3OTExYjI4ZWIxMGJkODFjZDp7fQ==','2014-08-01 13:41:38'),('6lc21iwv32lwyasfhduii8zgn5rcqip8','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-03 13:10:29'),('7qzsouxo52dh5wajset8s91tys5azta3','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-02 09:31:31'),('aossf3pfckr277tptokgx0m7bhl4ufo2','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-02 12:05:56'),('eji2e0my1vced38qb13nb7w7s4pdu1vr','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-03 02:31:08'),('kfhyg5dlsggqqt4q2yz2yu5kxlhdr57n','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-02 14:58:55'),('l37odvikwi0bs45q4pyqlk9l3f3ei08f','MTk3Y2Q2YTE1YjZmZjYwNzE2MjAxYmMyNWQwMDhkZjVhYWI1N2ZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-07-31 04:32:37'),('l721ddyjslrssmg4d54loax9jg8id7cf','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-06 02:21:24'),('lbcn4eyaisi0ccx89wqufo4462s1169r','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-06 03:03:30'),('nct21w1a29isfvojb6je6eip5x2qc9nv','Y2RjYzc2MDdkNGFmNjU1N2IzMmVjNmExODAwZWExNTBjMGJiOWE4Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-08-03 13:53:14'),('nyz7h15ol5n45kl2w8w5dkbks3e2n7mo','YWJhZTNmNTUwNzU1NTc2YTlkYWRmOTA5MzBjYzVlNTZlOTVhYjY0MTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Nn0=','2014-08-03 14:06:23'),('o3g6dopvxhhvk6lj98ausltyfxs0tm2w','YWJhZTNmNTUwNzU1NTc2YTlkYWRmOTA5MzBjYzVlNTZlOTVhYjY0MTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Nn0=','2014-08-01 09:19:40'),('qzq7bc5q2342nhprbv0dmdpf76ohxp9h','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-01 11:53:14'),('roylhvfhbr31w283ev0dly2cjzucl556','MTk3Y2Q2YTE1YjZmZjYwNzE2MjAxYmMyNWQwMDhkZjVhYWI1N2ZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-08-01 05:40:03'),('sgu7mnl91whizmzrzunm0tpx6xjosi4z','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-06 04:48:04'),('sj55noa2da5ahe774nyoae5cqzhl8nti','MjhlZjA0MTEwMjM4YWQ2NmM3ZTM4ZDBmMTlhYTNhMTQ2ODg3M2UyZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2014-08-06 02:15:07'),('throodj1y62begti3xdru1k2pboe3tu6','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-01 12:05:26'),('tuweuum3l71xd6obgwq12pstjvcdpqrx','MWMxYzU2M2M0YWQ2YzkyNWNkY2M5MmQyMjVmMzg2OTA3Yjg3ZGY1MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NH0=','2014-08-05 15:00:38'),('ws74t6glov1h569n097irgzhhzrsuuwr','MjhlZjA0MTEwMjM4YWQ2NmM3ZTM4ZDBmMTlhYTNhMTQ2ODg3M2UyZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2014-08-01 07:56:30');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_askforfriendmessage`
--

DROP TABLE IF EXISTS `picwall_askforfriendmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_askforfriendmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `state` varchar(10) NOT NULL,
  `ask_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_askforfriendmessage_0a681a64` (`sender_id`),
  KEY `picwall_askforfriendmessage_066c7a30` (`receiver_id`),
  CONSTRAINT `receiver_id_refs_id_f286ba58` FOREIGN KEY (`receiver_id`) REFERENCES `picwall_websiteuser` (`id`),
  CONSTRAINT `sender_id_refs_id_f286ba58` FOREIGN KEY (`sender_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_askforfriendmessage`
--

LOCK TABLES `picwall_askforfriendmessage` WRITE;
/*!40000 ALTER TABLE `picwall_askforfriendmessage` DISABLE KEYS */;
INSERT INTO `picwall_askforfriendmessage` VALUES (2,3,5,'accept','2014-07-20'),(3,3,4,'wait','2014-07-20'),(4,3,5,'accept','2014-07-20'),(5,4,5,'accept','2014-07-20'),(6,4,3,'refuse','2014-07-20'),(7,6,3,'accept','2014-07-20'),(8,6,4,'wait','2014-07-20'),(9,6,5,'accept','2014-07-20');
/*!40000 ALTER TABLE `picwall_askforfriendmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_photoinformation`
--

DROP TABLE IF EXISTS `picwall_photoinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_photoinformation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `picture_id` int(11) NOT NULL,
  `photowall_id` int(11) NOT NULL,
  `left` varchar(16) NOT NULL,
  `top` varchar(16) NOT NULL,
  `width` varchar(16) NOT NULL,
  `height` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_photoinformation_8fb8778b` (`picture_id`),
  KEY `picwall_photoinformation_c450f095` (`photowall_id`),
  CONSTRAINT `photowall_id_refs_id_77db06ec` FOREIGN KEY (`photowall_id`) REFERENCES `picwall_photowall` (`id`),
  CONSTRAINT `picture_id_refs_id_97739d7f` FOREIGN KEY (`picture_id`) REFERENCES `picwall_picture` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photoinformation`
--

LOCK TABLES `picwall_photoinformation` WRITE;
/*!40000 ALTER TABLE `picwall_photoinformation` DISABLE KEYS */;
INSERT INTO `picwall_photoinformation` VALUES (77,4,14,'774px','317.767px','196px','276px'),(78,4,14,'358.067px','171.6px','196px','277px'),(79,4,14,'547.067px','92.6px','196px','277px'),(80,4,14,'385.067px','98.6px','196px','277px'),(81,4,14,'486.067px','245.6px','196px','277px'),(82,5,14,'250.25px','139.417px','194px','279px');
/*!40000 ALTER TABLE `picwall_photoinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_photowall`
--

DROP TABLE IF EXISTS `picwall_photowall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_photowall` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `description` varchar(256) NOT NULL,
  `create_date` date NOT NULL,
  `modify_date` date NOT NULL,
  `access_times` int(11) NOT NULL,
  `access_permission` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_photowall_ad376f8d` (`creator_id`),
  CONSTRAINT `creator_id_refs_id_98b3c643` FOREIGN KEY (`creator_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowall`
--

LOCK TABLES `picwall_photowall` WRITE;
/*!40000 ALTER TABLE `picwall_photowall` DISABLE KEYS */;
INSERT INTO `picwall_photowall` VALUES (14,'',3,'','2014-07-23','2014-07-23',115,'private'),(15,'pw',3,'','2014-07-23','2014-07-23',3,'private'),(16,'pw2',3,'','2014-07-23','2014-07-23',0,'private'),(17,'pw3',3,'','2014-07-23','2014-07-23',0,'private'),(18,'pwww',5,'','2014-07-23','2014-07-23',11,'private');
/*!40000 ALTER TABLE `picwall_photowall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_photowall_access_users`
--

DROP TABLE IF EXISTS `picwall_photowall_access_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_photowall_access_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photowall_id` int(11) NOT NULL,
  `websiteuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `picwall_photowall_access_users_photowall_id_2a11c1a7_uniq` (`photowall_id`,`websiteuser_id`),
  KEY `picwall_photowall_access_users_c450f095` (`photowall_id`),
  KEY `picwall_photowall_access_users_44c649b3` (`websiteuser_id`),
  CONSTRAINT `photowall_id_refs_id_e48d0cae` FOREIGN KEY (`photowall_id`) REFERENCES `picwall_photowall` (`id`),
  CONSTRAINT `websiteuser_id_refs_id_2d60dc01` FOREIGN KEY (`websiteuser_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowall_access_users`
--

LOCK TABLES `picwall_photowall_access_users` WRITE;
/*!40000 ALTER TABLE `picwall_photowall_access_users` DISABLE KEYS */;
INSERT INTO `picwall_photowall_access_users` VALUES (17,14,3),(18,15,3),(19,16,3),(20,17,3),(21,18,5);
/*!40000 ALTER TABLE `picwall_photowall_access_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_photowall_manage_users`
--

DROP TABLE IF EXISTS `picwall_photowall_manage_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_photowall_manage_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photowall_id` int(11) NOT NULL,
  `websiteuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `picwall_photowall_manage_users_photowall_id_73849c4a_uniq` (`photowall_id`,`websiteuser_id`),
  KEY `picwall_photowall_manage_users_c450f095` (`photowall_id`),
  KEY `picwall_photowall_manage_users_44c649b3` (`websiteuser_id`),
  CONSTRAINT `photowall_id_refs_id_2c33610f` FOREIGN KEY (`photowall_id`) REFERENCES `picwall_photowall` (`id`),
  CONSTRAINT `websiteuser_id_refs_id_0c8a66ae` FOREIGN KEY (`websiteuser_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowall_manage_users`
--

LOCK TABLES `picwall_photowall_manage_users` WRITE;
/*!40000 ALTER TABLE `picwall_photowall_manage_users` DISABLE KEYS */;
INSERT INTO `picwall_photowall_manage_users` VALUES (21,14,3),(22,15,3),(23,16,3),(24,17,3),(25,18,5);
/*!40000 ALTER TABLE `picwall_photowall_manage_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_photowallcomment`
--

DROP TABLE IF EXISTS `picwall_photowallcomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_photowallcomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pw_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `content` varchar(100) NOT NULL,
  `published_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_photowallcomment_64814f1c` (`pw_id`),
  KEY `picwall_photowallcomment_e969df21` (`author_id`),
  CONSTRAINT `author_id_refs_id_fb6c4bc9` FOREIGN KEY (`author_id`) REFERENCES `picwall_websiteuser` (`id`),
  CONSTRAINT `pw_id_refs_id_c3918881` FOREIGN KEY (`pw_id`) REFERENCES `picwall_photowall` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowallcomment`
--

LOCK TABLES `picwall_photowallcomment` WRITE;
/*!40000 ALTER TABLE `picwall_photowallcomment` DISABLE KEYS */;
INSERT INTO `picwall_photowallcomment` VALUES (1,18,5,'aa','2014-07-23'),(2,18,5,'a','2014-07-23');
/*!40000 ALTER TABLE `picwall_photowallcomment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_picture`
--

DROP TABLE IF EXISTS `picwall_picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `description` varchar(64) NOT NULL,
  `upload_time` datetime NOT NULL,
  `author_id` int(11) NOT NULL,
  `label_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_picture_e969df21` (`author_id`),
  KEY `picwall_picture_e05256b6` (`label_id`),
  CONSTRAINT `author_id_refs_id_481d8ada` FOREIGN KEY (`author_id`) REFERENCES `picwall_websiteuser` (`id`),
  CONSTRAINT `label_id_refs_id_80f8685f` FOREIGN KEY (`label_id`) REFERENCES `picwall_picturelabel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_picture`
--

LOCK TABLES `picwall_picture` WRITE;
/*!40000 ALTER TABLE `picwall_picture` DISABLE KEYS */;
INSERT INTO `picwall_picture` VALUES (3,'','','2014-07-23 02:11:38',7,8),(4,'','','2014-07-23 02:41:51',3,3),(5,'范冰冰2','','2014-07-23 04:29:06',3,3),(6,'','','2014-07-23 05:13:26',3,3);
/*!40000 ALTER TABLE `picwall_picture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_picturecomment`
--

DROP TABLE IF EXISTS `picwall_picturecomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_picturecomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pic_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `content` varchar(100) NOT NULL,
  `published_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_picturecomment_e2c316d2` (`pic_id`),
  KEY `picwall_picturecomment_e969df21` (`author_id`),
  CONSTRAINT `author_id_refs_id_4ed4c138` FOREIGN KEY (`author_id`) REFERENCES `picwall_websiteuser` (`id`),
  CONSTRAINT `pic_id_refs_id_2484ee60` FOREIGN KEY (`pic_id`) REFERENCES `picwall_picture` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_picturecomment`
--

LOCK TABLES `picwall_picturecomment` WRITE;
/*!40000 ALTER TABLE `picwall_picturecomment` DISABLE KEYS */;
/*!40000 ALTER TABLE `picwall_picturecomment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_picturelabel`
--

DROP TABLE IF EXISTS `picwall_picturelabel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_picturelabel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_picturelabel_cb902d83` (`owner_id`),
  CONSTRAINT `owner_id_refs_id_c34b4ad9` FOREIGN KEY (`owner_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_picturelabel`
--

LOCK TABLES `picwall_picturelabel` WRITE;
/*!40000 ALTER TABLE `picwall_picturelabel` DISABLE KEYS */;
INSERT INTO `picwall_picturelabel` VALUES (3,'default',3),(4,'default',4),(5,'default',5),(6,'label',3),(7,'default',6),(8,'default',7);
/*!40000 ALTER TABLE `picwall_picturelabel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_websiteuser`
--

DROP TABLE IF EXISTS `picwall_websiteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_websiteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_websiteuser_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_18605a51` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_websiteuser`
--

LOCK TABLES `picwall_websiteuser` WRITE;
/*!40000 ALTER TABLE `picwall_websiteuser` DISABLE KEYS */;
INSERT INTO `picwall_websiteuser` VALUES (3,4),(4,5),(5,6),(6,7),(7,8);
/*!40000 ALTER TABLE `picwall_websiteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_websiteuser_friends`
--

DROP TABLE IF EXISTS `picwall_websiteuser_friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_websiteuser_friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_websiteuser_id` int(11) NOT NULL,
  `to_websiteuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `picwall_websiteuser_friends_from_websiteuser_id_79288c0d_uniq` (`from_websiteuser_id`,`to_websiteuser_id`),
  KEY `picwall_websiteuser_friends_d5fb8d64` (`from_websiteuser_id`),
  KEY `picwall_websiteuser_friends_9ac1ceca` (`to_websiteuser_id`),
  CONSTRAINT `from_websiteuser_id_refs_id_68200e56` FOREIGN KEY (`from_websiteuser_id`) REFERENCES `picwall_websiteuser` (`id`),
  CONSTRAINT `to_websiteuser_id_refs_id_68200e56` FOREIGN KEY (`to_websiteuser_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_websiteuser_friends`
--

LOCK TABLES `picwall_websiteuser_friends` WRITE;
/*!40000 ALTER TABLE `picwall_websiteuser_friends` DISABLE KEYS */;
INSERT INTO `picwall_websiteuser_friends` VALUES (10,3,5),(13,3,6),(12,4,5),(9,5,3),(11,5,4),(15,5,6),(14,6,3),(16,6,5);
/*!40000 ALTER TABLE `picwall_websiteuser_friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'picwall','0001_initial','2014-07-17 04:30:34'),(2,'picwall','0002_auto__del_field_picture_image','2014-07-17 04:38:07'),(3,'picwall','0003_auto__add_field_photowall_access_permission','2014-07-18 06:20:44'),(4,'picwall','0004_auto__add_askforfriendmessage','2014-07-18 16:19:10'),(5,'picwall','0005_auto__add_field_askforfriendmessage_ask_data__add_field_askforfriendme','2014-07-20 12:07:32'),(6,'picwall','0006_auto__del_field_askforfriendmessage_ask_data__add_field_askforfriendme','2014-07-20 12:08:01'),(7,'picwall','0007_auto__add_photowallcomment','2014-07-23 05:29:24');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-07-23 13:36:36
