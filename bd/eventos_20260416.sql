-- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
--
-- Host: localhost    Database: eventos
-- ------------------------------------------------------
-- Server version	8.0.45-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add evento',7,'add_evento'),(26,'Can change evento',7,'change_evento'),(27,'Can delete evento',7,'delete_evento'),(28,'Can view evento',7,'view_evento'),(29,'Can add participante',8,'add_participante'),(30,'Can change participante',8,'change_participante'),(31,'Can delete participante',8,'delete_participante'),(32,'Can view participante',8,'view_participante'),(33,'Can add premiacion',9,'add_premiacion'),(34,'Can change premiacion',9,'change_premiacion'),(35,'Can delete premiacion',9,'delete_premiacion'),(36,'Can view premiacion',9,'view_premiacion'),(37,'Can add presupuesto',10,'add_presupuesto'),(38,'Can change presupuesto',10,'change_presupuesto'),(39,'Can delete presupuesto',10,'delete_presupuesto'),(40,'Can view presupuesto',10,'view_presupuesto');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'registrar_eventos','evento'),(8,'registrar_eventos','participante'),(9,'registrar_eventos','premiacion'),(10,'registrar_eventos','presupuesto'),(5,'sessions','session'),(6,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-04-16 19:46:57.300520'),(2,'contenttypes','0002_remove_content_type_name','2026-04-16 19:46:57.391396'),(3,'auth','0001_initial','2026-04-16 19:46:57.633450'),(4,'auth','0002_alter_permission_name_max_length','2026-04-16 19:46:57.705867'),(5,'auth','0003_alter_user_email_max_length','2026-04-16 19:46:57.711885'),(6,'auth','0004_alter_user_username_opts','2026-04-16 19:46:57.717767'),(7,'auth','0005_alter_user_last_login_null','2026-04-16 19:46:57.725341'),(8,'auth','0006_require_contenttypes_0002','2026-04-16 19:46:57.730071'),(9,'auth','0007_alter_validators_add_error_messages','2026-04-16 19:46:57.741497'),(10,'auth','0008_alter_user_username_max_length','2026-04-16 19:46:57.747375'),(11,'auth','0009_alter_user_last_name_max_length','2026-04-16 19:46:57.757456'),(12,'auth','0010_alter_group_name_max_length','2026-04-16 19:46:57.775178'),(13,'auth','0011_update_proxy_permissions','2026-04-16 19:46:57.786044'),(14,'auth','0012_alter_user_first_name_max_length','2026-04-16 19:46:57.791723'),(15,'users','0001_initial','2026-04-16 19:46:57.987937'),(16,'admin','0001_initial','2026-04-16 19:46:58.090825'),(17,'admin','0002_logentry_remove_auto_add','2026-04-16 19:46:58.097654'),(18,'admin','0003_logentry_add_action_flag_choices','2026-04-16 19:46:58.104367'),(19,'registrar_eventos','0001_initial','2026-04-16 19:46:58.289636'),(20,'registrar_eventos','0002_alter_evento_fecha_actividad_and_more','2026-04-16 19:46:58.394014'),(21,'sessions','0001_initial','2026-04-16 19:46:58.441431');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('qrw6bm1p5copwjs7wmhqko1cemwx7xx7','.eJxVjMsOwiAQRf-FtSEwIA-X7v0GMjAgVQNJaVfGf7dNutDtOefeNwu4LjWsI89hInZhkp1-WcT0zG0X9MB27zz1tsxT5HvCDzv4rVN-XY_276DiqNtagZU-gk8mGzQFkpPgUHhByhQpgQoRGDoLkGQxk3ZWFafQKL1R0uzzBc6zN3E:1wDSgh:J9X3BcddCP9iK1T3A0rArLZXl10J7Qp1_W-XyGook4s','2026-04-30 19:47:43.296734');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrar_eventos_evento`
--

DROP TABLE IF EXISTS `registrar_eventos_evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrar_eventos_evento` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `agencia` varchar(100) NOT NULL,
  `fecha_informe` date NOT NULL,
  `tipo_actividad` varchar(100) NOT NULL,
  `nombre_actividad` longtext NOT NULL,
  `fecha_actividad` date NOT NULL,
  `lugar_actividad` varchar(255) NOT NULL,
  `cupo_participantes` int NOT NULL,
  `asociados_participantes` int NOT NULL,
  `acompanantes_participantes` int NOT NULL,
  `facilitador` longtext NOT NULL,
  `entidad_aliada` longtext NOT NULL,
  `programa_desarrollo` longtext NOT NULL,
  `descripcion_ejecucion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrar_eventos_evento`
--

LOCK TABLES `registrar_eventos_evento` WRITE;
/*!40000 ALTER TABLE `registrar_eventos_evento` DISABLE KEYS */;
/*!40000 ALTER TABLE `registrar_eventos_evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrar_eventos_participante`
--

DROP TABLE IF EXISTS `registrar_eventos_participante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrar_eventos_participante` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_participante` varchar(20) NOT NULL,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `identificacion` varchar(50) NOT NULL,
  `agencia` varchar(100) NOT NULL,
  `evento_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registrar_eventos_pa_evento_id_49ae856c_fk_registrar` (`evento_id`),
  CONSTRAINT `registrar_eventos_pa_evento_id_49ae856c_fk_registrar` FOREIGN KEY (`evento_id`) REFERENCES `registrar_eventos_evento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrar_eventos_participante`
--

LOCK TABLES `registrar_eventos_participante` WRITE;
/*!40000 ALTER TABLE `registrar_eventos_participante` DISABLE KEYS */;
/*!40000 ALTER TABLE `registrar_eventos_participante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrar_eventos_premiacion`
--

DROP TABLE IF EXISTS `registrar_eventos_premiacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrar_eventos_premiacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `identificacion` varchar(50) NOT NULL,
  `agencia` varchar(100) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `puesto_numero` int NOT NULL,
  `valor_premio` decimal(12,2) NOT NULL,
  `evento_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registrar_eventos_pr_evento_id_08884cc8_fk_registrar` (`evento_id`),
  CONSTRAINT `registrar_eventos_pr_evento_id_08884cc8_fk_registrar` FOREIGN KEY (`evento_id`) REFERENCES `registrar_eventos_evento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrar_eventos_premiacion`
--

LOCK TABLES `registrar_eventos_premiacion` WRITE;
/*!40000 ALTER TABLE `registrar_eventos_premiacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `registrar_eventos_premiacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrar_eventos_presupuesto`
--

DROP TABLE IF EXISTS `registrar_eventos_presupuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrar_eventos_presupuesto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(20) NOT NULL,
  `refrigerio` decimal(10,2) NOT NULL,
  `almuerzo` decimal(10,2) NOT NULL,
  `publicidad` decimal(10,2) NOT NULL,
  `sonido` decimal(10,2) NOT NULL,
  `video` decimal(10,2) NOT NULL,
  `premiacion` decimal(10,2) NOT NULL,
  `imprevistos` decimal(10,2) NOT NULL,
  `otros` decimal(10,2) NOT NULL,
  `valor_proyecto` decimal(12,2) NOT NULL,
  `total_presupuesto` decimal(12,2) NOT NULL,
  `evento_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `registrar_eventos_pr_evento_id_1acec824_fk_registrar` (`evento_id`),
  CONSTRAINT `registrar_eventos_pr_evento_id_1acec824_fk_registrar` FOREIGN KEY (`evento_id`) REFERENCES `registrar_eventos_evento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrar_eventos_presupuesto`
--

LOCK TABLES `registrar_eventos_presupuesto` WRITE;
/*!40000 ALTER TABLE `registrar_eventos_presupuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `registrar_eventos_presupuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `identificacion` varchar(100) NOT NULL,
  `nombres` varchar(255) NOT NULL,
  `agencia` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `identificacion` (`identificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$1000000$gGM1FzsONBlrbZixlAjBsb$oicShjZgO/pLwUDNnAoh1g2pHW1Dyky0r+zQh26YmbU=','2026-04-16 19:47:43.292230',1,'admin11','','','soportesistemas@cootep.com.co',1,1,'2026-04-16 19:47:24.180131','','','');
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-16 14:52:22
