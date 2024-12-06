-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 06 déc. 2024 à 19:37
-- Version du serveur : 8.0.40
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `todo_app`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add task', 7, 'add_task'),
(26, 'Can change task', 7, 'change_task'),
(27, 'Can delete task', 7, 'delete_task'),
(28, 'Can view task', 7, 'view_task'),
(29, 'Can add task list', 8, 'add_tasklist'),
(30, 'Can change task list', 8, 'change_tasklist'),
(31, 'Can delete task list', 8, 'delete_tasklist'),
(32, 'Can view task list', 8, 'view_tasklist'),
(33, 'Can add user profile', 9, 'add_userprofile'),
(34, 'Can change user profile', 9, 'change_userprofile'),
(35, 'Can delete user profile', 9, 'delete_userprofile'),
(36, 'Can view user profile', 9, 'view_userprofile'),
(37, 'Can add profile', 10, 'add_profile'),
(38, 'Can change profile', 10, 'change_profile'),
(39, 'Can delete profile', 10, 'delete_profile'),
(40, 'Can view profile', 10, 'view_profile');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$O742x2dgxLBtTf5RMFXvij$XACgKAC7a5B5rpNGOrk+pIA9/IvEFjFtWH3sqNU79ew=', '2024-12-06 18:54:35.509491', 1, 'hppavillion', '', '', 'meyladjabeee@gmail.com', 1, 1, '2024-12-05 21:10:47.724520'),
(3, 'pbkdf2_sha256$870000$9FZ45cP3vuMhpoDJvx43Za$rf7jraSBb402xb2V3rHCXKxvLGk4cjbmnGoGG/C1ics=', NULL, 0, 'mey1234', '', '', 'meyladjabeee@gmail.com', 0, 1, '2024-12-05 21:45:34.617963'),
(4, 'pbkdf2_sha256$870000$UYdFmE7aJNKSbTQa6X0DD4$TVByGSnSNED6rkWb8vVuUwwN6clkiPoy5MqngwsHV8o=', NULL, 0, 'mimii145', '', '', 'kjezkjdhkj@gmail.com', 0, 1, '2024-12-06 17:05:37.104910');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-12-05 21:12:50.620514', '2', 'mey123', 1, '[{\"added\": {}}]', 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(10, 'todo_app', 'profile'),
(7, 'todo_app', 'task'),
(8, 'todo_app', 'tasklist'),
(9, 'todo_app', 'userprofile');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-12-01 17:12:15.285704'),
(2, 'auth', '0001_initial', '2024-12-01 17:12:16.461857'),
(3, 'admin', '0001_initial', '2024-12-01 17:12:16.715752'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-12-01 17:12:16.734712'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-01 17:12:16.759545'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-12-01 17:12:16.912824'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-12-01 17:12:17.020863'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-12-01 17:12:17.068951'),
(9, 'auth', '0004_alter_user_username_opts', '2024-12-01 17:12:17.079389'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-12-01 17:12:17.164172'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-12-01 17:12:17.169163'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-12-01 17:12:17.187888'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-12-01 17:12:17.306971'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-12-01 17:12:17.432605'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-12-01 17:12:17.477600'),
(16, 'auth', '0011_update_proxy_permissions', '2024-12-01 17:12:17.500608'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-12-01 17:12:17.622418'),
(18, 'sessions', '0001_initial', '2024-12-01 17:12:17.691396'),
(19, 'todo_app', '0001_initial', '2024-12-01 17:12:17.769882'),
(20, 'todo_app', '0002_userprofile', '2024-12-01 17:12:17.910914'),
(21, 'todo_app', '0003_profile_delete_userprofile', '2024-12-05 21:43:39.232819'),
(22, 'todo_app', '0004_profile_full_name', '2024-12-05 21:56:33.895891');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('uqag9ouy0cnh3ctqpi83omu4pv53cxg9', '.eJxVjEEOwiAQRe_C2hBBhg4u3fcMZJhBqRpISrsy3l2bdKHb_977LxVpXUpce57jJOqsjDr8bon4kesG5E711jS3usxT0puid9r12CQ_L7v7d1Col2_tOQGT8QLAAoLOe0EiujrAgBySI0YzIACdkk2DQDh6i2ANWyds1fsD9cM32g:1tJdTH:3VfCuKs0xofcxZ4V5yknjFiNa8lmAwkkEvnIalBke7M', '2024-12-20 18:54:35.517476'),
('y90sovbxfnvpsdkl0th032bsthswo11f', '.eJxVjEEOwiAQRe_C2hBBhg4u3fcMZJhBqRpISrsy3l2bdKHb_977LxVpXUpce57jJOqsjDr8bon4kesG5E711jS3usxT0puid9r12CQ_L7v7d1Col2_tOQGT8QLAAoLOe0EiujrAgBySI0YzIACdkk2DQDh6i2ANWyds1fsD9cM32g:1tJdTG:ycCmLMNh4mxjHU9Tl7opNazIDHN_7pWKN_CHetdfV90', '2024-12-20 18:54:34.523966');

-- --------------------------------------------------------

--
-- Structure de la table `todo_app_profile`
--

DROP TABLE IF EXISTS `todo_app_profile`;
CREATE TABLE IF NOT EXISTS `todo_app_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `country` varchar(100) NOT NULL,
  `user_id` int NOT NULL,
  `full_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `todo_app_profile`
--

INSERT INTO `todo_app_profile` (`id`, `address`, `phone`, `country`, `user_id`, `full_name`) VALUES
(1, '', '', '', 3, ''),
(2, '', '', '', 4, '');

-- --------------------------------------------------------

--
-- Structure de la table `todo_app_task`
--

DROP TABLE IF EXISTS `todo_app_task`;
CREATE TABLE IF NOT EXISTS `todo_app_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `priority` varchar(10) NOT NULL,
  `category` varchar(100) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `status` varchar(15) NOT NULL,
  `due_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `todo_app_task`
--

INSERT INTO `todo_app_task` (`id`, `name`, `priority`, `category`, `start_time`, `end_time`, `status`, `due_date`) VALUES
(1, 'ksdjd', 'Low', 'kdjdk', '2024-12-18 18:13:00.000000', '2025-01-08 18:13:00.000000', 'Processing', '2024-12-08 17:13:21.659736'),
(2, 'ldkfkd', 'High', 'dkfd', '2024-12-02 20:21:00.000000', '2024-12-03 20:21:00.000000', 'Cancelled', '2024-12-08 19:21:25.787219'),
(3, 'sejgoisdjg', 'Medium', 'mdsgpsop', '2024-12-04 08:14:00.000000', '2024-12-05 08:14:00.000000', 'Finished', '2024-12-09 07:14:57.356475'),
(4, 'oidshfoeziehf', 'Medium', 'school', '2024-12-11 09:52:00.000000', '2024-12-17 09:52:00.000000', 'Processing', '2024-12-09 08:52:49.480056'),
(5, 'pecho bateman', 'High', 'Q', '2024-12-02 17:47:00.000000', '2025-12-02 17:47:00.000000', 'Processing', '2024-12-09 16:48:07.098914');

-- --------------------------------------------------------

--
-- Structure de la table `todo_app_tasklist`
--

DROP TABLE IF EXISTS `todo_app_tasklist`;
CREATE TABLE IF NOT EXISTS `todo_app_tasklist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `todo_app_profile`
--
ALTER TABLE `todo_app_profile`
  ADD CONSTRAINT `todo_app_profile_user_id_a398d428_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
