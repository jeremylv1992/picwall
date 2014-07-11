-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: picwallDB
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add web site user',8,'add_websiteuser'),(23,'Can change web site user',8,'change_websiteuser'),(24,'Can delete web site user',8,'delete_websiteuser'),(25,'Can add picture',9,'add_picture'),(26,'Can change picture',9,'change_picture'),(27,'Can delete picture',9,'delete_picture'),(28,'Can add picture comment',10,'add_picturecomment'),(29,'Can change picture comment',10,'change_picturecomment'),(30,'Can delete picture comment',10,'delete_picturecomment'),(31,'Can add photo wall',11,'add_photowall'),(32,'Can change photo wall',11,'change_photowall'),(33,'Can delete photo wall',11,'delete_photowall'),(34,'Can add photo information',12,'add_photoinformation'),(35,'Can change photo information',12,'change_photoinformation'),(36,'Can delete photo information',12,'delete_photoinformation'),(37,'Can add migration history',13,'add_migrationhistory'),(38,'Can change migration history',13,'change_migrationhistory'),(39,'Can delete migration history',13,'delete_migrationhistory');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$ZGRyakwnw0BF$f/wiu8hGYYIBN76bs9rkHOXFxbkoInL5/NpBAbQoJQI=','2014-07-11 00:54:25',1,'root','','','',1,1,'2014-07-10 07:56:24'),(2,'pbkdf2_sha256$12000$E1Od1dOsb1Uk$0JlEndTlhtq4foUMStVTluHtQgCBHuuuafo/GyQQORk=','2014-07-11 00:55:06',0,'a','','','a@b.c',0,1,'2014-07-10 08:00:53'),(3,'pbkdf2_sha256$12000$cX6Z1c3Ei8Fp$i97ZSmWGdcV5hIqcmLgeL6M1daj/bi37dvEv7cxZMLw=','2014-07-10 13:39:16',0,'pw','','','d@e.c',0,1,'2014-07-10 13:24:46');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-07-10 08:41:21',1,11,'1','',3,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'web site user','picwall','websiteuser'),(9,'picture','picwall','picture'),(10,'picture comment','picwall','picturecomment'),(11,'photo wall','picwall','photowall'),(12,'photo information','picwall','photoinformation'),(13,'migration history','south','migrationhistory');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('506xzwab77j7kgumrjth79vp7jd65ltj','MTk3Y2Q2YTE1YjZmZjYwNzE2MjAxYmMyNWQwMDhkZjVhYWI1N2ZkMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-07-25 00:55:06');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photoinformation`
--

LOCK TABLES `picwall_photoinformation` WRITE;
/*!40000 ALTER TABLE `picwall_photoinformation` DISABLE KEYS */;
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
  `access_times` int(11) NOT NULL,
  `create_date` date NOT NULL,
  `modify_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_photowall_ad376f8d` (`creator_id`),
  CONSTRAINT `creator_id_refs_id_98b3c643` FOREIGN KEY (`creator_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowall`
--

LOCK TABLES `picwall_photowall` WRITE;
/*!40000 ALTER TABLE `picwall_photowall` DISABLE KEYS */;
INSERT INTO `picwall_photowall` VALUES (6,'pw',1,'',0,'2014-07-10','2014-07-10');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowall_access_users`
--

LOCK TABLES `picwall_photowall_access_users` WRITE;
/*!40000 ALTER TABLE `picwall_photowall_access_users` DISABLE KEYS */;
INSERT INTO `picwall_photowall_access_users` VALUES (6,6,1);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_photowall_manage_users`
--

LOCK TABLES `picwall_photowall_manage_users` WRITE;
/*!40000 ALTER TABLE `picwall_photowall_manage_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `picwall_photowall_manage_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picwall_picture`
--

DROP TABLE IF EXISTS `picwall_picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picwall_picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `upload_time` datetime NOT NULL,
  `author_id` int(11) NOT NULL,
  `pid` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_picture_e969df21` (`author_id`),
  CONSTRAINT `author_id_refs_id_481d8ada` FOREIGN KEY (`author_id`) REFERENCES `picwall_websiteuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_picture`
--

LOCK TABLES `picwall_picture` WRITE;
/*!40000 ALTER TABLE `picwall_picture` DISABLE KEYS */;
INSERT INTO `picwall_picture` VALUES (12,'christmas','2014-07-11 01:22:54',1,'Thu_Jul_10_20_22_54_2014_christmas_a','');
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
  `content` varchar(100) NOT NULL,
  `author_id` int(11) NOT NULL,
  `pic_id` int(11) NOT NULL,
  `published_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `picwall_picturecomment_e969df21` (`author_id`),
  KEY `picwall_picturecomment_e2c316d2` (`pic_id`),
  CONSTRAINT `author_id_refs_id_4ed4c138` FOREIGN KEY (`author_id`) REFERENCES `picwall_websiteuser` (`id`),
  CONSTRAINT `pic_id_refs_id_2484ee60` FOREIGN KEY (`pic_id`) REFERENCES `picwall_picture` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_picturecomment`
--

LOCK TABLES `picwall_picturecomment` WRITE;
/*!40000 ALTER TABLE `picwall_picturecomment` DISABLE KEYS */;
INSERT INTO `picwall_picturecomment` VALUES (1,'a',1,12,'2014-07-10'),(2,'b',1,12,'2014-07-10');
/*!40000 ALTER TABLE `picwall_picturecomment` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_websiteuser`
--

LOCK TABLES `picwall_websiteuser` WRITE;
/*!40000 ALTER TABLE `picwall_websiteuser` DISABLE KEYS */;
INSERT INTO `picwall_websiteuser` VALUES (1,2),(2,3);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picwall_websiteuser_friends`
--

LOCK TABLES `picwall_websiteuser_friends` WRITE;
/*!40000 ALTER TABLE `picwall_websiteuser_friends` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'picwall','0002_auto__del_photoinformation__del_picture__del_photowall__del_websiteuse','2014-07-10 07:58:50'),(2,'picwall','0003_auto__add_photoinformation__add_picture__add_websiteuser__add_picturec','2014-07-10 07:59:12'),(3,'picwall','0004_auto__add_field_photowall_modify_data','2014-07-10 08:33:16'),(4,'picwall','0005_auto__del_field_picture_file_name__add_field_picture_pid','2014-07-10 08:40:55'),(5,'picwall','0006_auto__add_field_photowall_access_times','2014-07-10 08:50:00'),(6,'picwall','0007_auto__del_field_picture_url__del_field_picture_desc__add_field_picture','2014-07-10 09:20:32');
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

-- Dump completed on 2014-07-11  9:51:02
