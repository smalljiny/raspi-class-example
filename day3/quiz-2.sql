CREATE TABLE `rooms` (
  `no` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`no`)
) COMMENT='방 정보 테이블';

CREATE TABLE `measurements` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `measuring_time` TIME NOT NULL,
  `room` INT UNSIGNED NOT NULL,
  `temperature` TINYINT NULL DEFAULT 0,
  `humidity` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) COMMENT = '센서 계측 데이터 테이블';

CREATE TABLE `alrams` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_time` TIME NOT NULL COMMENT '알람 발생 시간',
  `type` CHAR(2) NOT NULL COMMENT '알람의 종류\n  - 온도\n  - 습도',
  `room` INT UNSIGNED NOT NULL COMMENT '방 번호',
  PRIMARY KEY (`id`)
) COMMENT = '알람 로그 테이블';

INSERT INTO `rooms` (`name`) VALUES ('안방'), ('옷방'), ('거실');

INSERT INTO `measurements` (`measuring_time`, `room`, `temperature`, `humidity`) VALUES ('16:01:00', 1, 2, 20);

INSERT INTO `alrams` (`created_time`, `type`, `room`) VALUES ('16:01:01', '습도', 2); 
