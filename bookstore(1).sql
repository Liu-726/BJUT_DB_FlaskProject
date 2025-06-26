/*
 Navicat Premium Dump SQL

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80405 (8.4.5)
 Source Host           : localhost:3306
 Source Schema         : bookstore

 Target Server Type    : MySQL
 Target Server Version : 80405 (8.4.5)
 File Encoding         : 65001

 Date: 25/06/2025 19:04:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book_info
-- ----------------------------
DROP TABLE IF EXISTS `book_info`;
CREATE TABLE `book_info`  (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_category` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `book_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `introduction` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`book_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 52 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of book_info
-- ----------------------------
INSERT INTO `book_info` VALUES (1, '心理学', '认知心理学手册', 55.83, '系统阐述认知过程与心理机制，心理学专业必备工具书。');
INSERT INTO `book_info` VALUES (2, '教育学习', 'monetize之旅', 33.64, '探索数字经济时代的变现策略与商业模式创新指南。');
INSERT INTO `book_info` VALUES (3, '计算机科学', 'C++实战', 126.86, '通过项目案例掌握C++11/14/17核心特性与开发技巧。');
INSERT INTO `book_info` VALUES (4, '旅游地理', 'synergize手册', 109.71, '企业协同增效方法论，提升团队效能的实践指南。');
INSERT INTO `book_info` VALUES (5, '文学小说', '冯的故事', 39.65, '一位抗战老兵跨越半个世纪的个人命运史诗。');
INSERT INTO `book_info` VALUES (6, '文学小说', '张的旅程', 112.18, '当代女性在职场与家庭间寻找自我的成长小说。');
INSERT INTO `book_info` VALUES (7, '艺术设计', 'engineer导论', 125.48, '工程师思维培养与系统工程基础概念入门。');
INSERT INTO `book_info` VALUES (8, '历史传记', 'synergize手册', 76.12, '跨部门协作的50个经典案例与解决方案汇编。');
INSERT INTO `book_info` VALUES (9, '旅游地理', 'empower之旅', 58.78, '自我赋能的心理训练手册，唤醒内在潜能。');
INSERT INTO `book_info` VALUES (10, '历史传记', 'morph艺术', 68.65, '数字媒体时代的视觉形态设计与动态表达。');
INSERT INTO `book_info` VALUES (11, '旅游地理', 'extend手册', 116.67, '软件扩展开发模式与插件体系架构详解。');
INSERT INTO `book_info` VALUES (12, '旅游地理', 'enhance艺术', 95.76, '摄影后期处理技术与视觉增强实战教程。');
INSERT INTO `book_info` VALUES (13, '教育学习', 'revolutionize手册', 147.38, '颠覆性创新者的思维模式与行业变革案例。');
INSERT INTO `book_info` VALUES (14, '心理学', '社会心理学手册', 144.80, '群体行为与社会认知研究的权威学术参考。');
INSERT INTO `book_info` VALUES (15, '心理学', '发展心理学导论', 112.45, '人类生命周期心理发展规律的专业教材。');
INSERT INTO `book_info` VALUES (16, '艺术设计', 'morph研究', 84.16, '生物形态学与计算机图形学的交叉学科探索。');
INSERT INTO `book_info` VALUES (17, '计算机科学', 'Python实战', 100.45, '从数据分析到机器学习项目全流程开发指南。');
INSERT INTO `book_info` VALUES (18, '健康养生', 're-contextualize研究', 121.02, '文化符号在数字时代的再语境化理论分析。');
INSERT INTO `book_info` VALUES (19, '历史传记', 'facilitate导论', 50.06, '会议引导技术与群体决策促进方法入门。');
INSERT INTO `book_info` VALUES (20, '心理学', '认知心理学应用', 132.09, '认知理论在教育与用户体验设计中的实践。');
INSERT INTO `book_info` VALUES (21, '旅游地理', 'aggregate之旅', 139.35, '大数据聚合分析技术与商业智能应用。');
INSERT INTO `book_info` VALUES (22, '历史传记', 'facilitate之旅', 35.67, '非营利组织社区工作 facilitation 技术手册。');
INSERT INTO `book_info` VALUES (23, '心理学', '社会心理学导论', 47.46, '社会态度与人际关系的基础理论教科书。');
INSERT INTO `book_info` VALUES (24, '历史传记', 'synthesize手册', 135.00, '学术论文写作中的文献综合方法与技巧。');
INSERT INTO `book_info` VALUES (25, '文学小说', '杨的回忆', 91.39, '民国知识分子的家国情怀与个人命运回忆录。');
INSERT INTO `book_info` VALUES (26, '科幻奇幻', '未来战争', 141.38, '人工智能与量子科技对军事战略的影响预测。');
INSERT INTO `book_info` VALUES (27, '健康养生', 'productize导论', 126.94, '科研成果产品化与市场化路径设计指南。');
INSERT INTO `book_info` VALUES (28, '科幻奇幻', '星际传奇', 35.41, '太阳系殖民时代的英雄史诗科幻小说。');
INSERT INTO `book_info` VALUES (29, '旅游地理', 'scale研究', 25.13, '企业规模化增长中的组织与管理挑战解析。');
INSERT INTO `book_info` VALUES (30, '心理学', '社会心理学手册', 46.23, '社会认知与群体行为研究最新成果汇编。');
INSERT INTO `book_info` VALUES (31, '心理学', '认知心理学研究', 25.62, '注意力与记忆机制的实验方法与发现。');
INSERT INTO `book_info` VALUES (32, '科幻奇幻', '时间之谜', 124.28, '探讨时间本质的物理学与哲学对话录。');
INSERT INTO `book_info` VALUES (33, '历史传记', 'incubate艺术', 68.83, '文创项目孵化与艺术创业实战手册。');
INSERT INTO `book_info` VALUES (34, '艺术设计', 'facilitate手册', 69.69, '敏捷开发中scrum master的 facilitation 技巧。');
INSERT INTO `book_info` VALUES (35, '健康养生', 'e-enable艺术', 57.61, '数字艺术创作工具与技术发展史图解。');
INSERT INTO `book_info` VALUES (36, '计算机科学', 'JavaScript实战', 37.78, '现代Web全栈开发与框架应用项目集。');
INSERT INTO `book_info` VALUES (37, '心理学', '社会心理学应用', 114.81, '社会心理效应在营销与管理中的运用。');
INSERT INTO `book_info` VALUES (38, '教育学习', 'embrace之旅', 61.62, '创伤后自我接纳与心理重建指导手册。');
INSERT INTO `book_info` VALUES (39, '悬疑推理', 'synergize研究', 86.44, '产学研协同创新机制的国际比较研究。');
INSERT INTO `book_info` VALUES (40, '艺术设计', 'innovate导论', 67.28, '设计思维与创新管理基础方法论。');
INSERT INTO `book_info` VALUES (41, '文学小说', '洪的回忆', 48.11, '南洋华侨商界领袖的创业史与家国叙事。');
INSERT INTO `book_info` VALUES (42, '健康养生', 'morph之旅', 129.44, '材料科学中的形态演变过程可视化研究。');
INSERT INTO `book_info` VALUES (43, '悬疑推理', 'orchestrate研究', 90.99, '复杂系统协调控制的理论与算法专著。');
INSERT INTO `book_info` VALUES (44, '科幻奇幻', '星际漫游', 99.56, '青少年太空探险题材的硬核科幻系列。');
INSERT INTO `book_info` VALUES (45, '心理学', '发展心理学研究', 101.53, '儿童语言习得与认知发展的纵向研究。');
INSERT INTO `book_info` VALUES (46, '心理学', '认知心理学手册', 72.15, '知觉与思维加工过程的实验心理学手册。');
INSERT INTO `book_info` VALUES (47, '历史传记', 'matrix艺术', 34.21, '算法生成艺术与数字矩阵美学探索。');
INSERT INTO `book_info` VALUES (48, '心理学', '情绪心理学导论', 81.68, '情绪产生机制与调节策略的学术入门。');
INSERT INTO `book_info` VALUES (49, '计算机科学', 'C++入门', 138.47, '零基础学习面向对象编程的图文教程。');
INSERT INTO `book_info` VALUES (51, '计算机科学', 'deploy导论', 87.23, '云原生应用部署与持续交付实践基础。');

-- ----------------------------
-- Table structure for buyer_info
-- ----------------------------
DROP TABLE IF EXISTS `buyer_info`;
CREATE TABLE `buyer_info`  (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` enum('男','女','其他') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `age` int NULL DEFAULT NULL,
  `contact` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`purchase_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 62 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of buyer_info
-- ----------------------------
INSERT INTO `buyer_info` VALUES (1, '李利', '其他', 46, '14582293682');
INSERT INTO `buyer_info` VALUES (2, '康波', '女', 57, '15956746886');
INSERT INTO `buyer_info` VALUES (3, '李建国', '女', 44, '13657323106');
INSERT INTO `buyer_info` VALUES (4, '覃红梅', '男', 31, '18909153579');
INSERT INTO `buyer_info` VALUES (5, '张欢', '女', 69, '18027732465');
INSERT INTO `buyer_info` VALUES (6, '许丹', '男', 37, '13109262971');
INSERT INTO `buyer_info` VALUES (7, '黄俊', '女', 32, '18176883988');
INSERT INTO `buyer_info` VALUES (8, '张秀珍', '女', 38, '18971317776');
INSERT INTO `buyer_info` VALUES (9, '甘雪', '男', 52, '18112777024');
INSERT INTO `buyer_info` VALUES (10, '迟伟', '女', 41, '18885159232');
INSERT INTO `buyer_info` VALUES (11, '李倩', '其他', 39, '13098416996');
INSERT INTO `buyer_info` VALUES (12, '陈涛', '女', 66, '15023230135');
INSERT INTO `buyer_info` VALUES (13, '彭静', '男', 36, '15050766177');
INSERT INTO `buyer_info` VALUES (14, '朱晶', '男', 44, '14510743006');
INSERT INTO `buyer_info` VALUES (15, '刘玉珍', '男', 70, '13155911402');
INSERT INTO `buyer_info` VALUES (16, '王玉梅', '女', 53, '15237360211');
INSERT INTO `buyer_info` VALUES (17, '丁畅', '女', 30, '15866906528');
INSERT INTO `buyer_info` VALUES (18, '丁倩', '女', 44, '13859477835');
INSERT INTO `buyer_info` VALUES (19, '马琴', '女', 34, '18537241645');
INSERT INTO `buyer_info` VALUES (20, '陈桂芳', '男', 47, '18803538079');

-- ----------------------------
-- Table structure for purchase_method
-- ----------------------------
DROP TABLE IF EXISTS `purchase_method`;
CREATE TABLE `purchase_method`  (
  `method_id` int NOT NULL AUTO_INCREMENT,
  `purchase_id` int NOT NULL,
  `book_id` int NOT NULL,
  `payment_method` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `delivery_method` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`method_id`) USING BTREE,
  INDEX `purchase_id`(`purchase_id` ASC) USING BTREE,
  INDEX `book_id`(`book_id` ASC) USING BTREE,
  CONSTRAINT `purchase_method_ibfk_1` FOREIGN KEY (`purchase_id`) REFERENCES `buyer_info` (`purchase_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `purchase_method_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book_info` (`book_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 102 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of purchase_method
-- ----------------------------
INSERT INTO `purchase_method` VALUES (1, 1, 20, '货到付款', '自提');
INSERT INTO `purchase_method` VALUES (2, 2, 27, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (3, 3, 38, '微信支付', '同城闪送');
INSERT INTO `purchase_method` VALUES (4, 4, 45, '微信支付', '快递');
INSERT INTO `purchase_method` VALUES (5, 5, 5, '银行卡', '自提');
INSERT INTO `purchase_method` VALUES (6, 6, 6, '信用卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (7, 7, 29, '信用卡', '自提');
INSERT INTO `purchase_method` VALUES (8, 8, 32, '货到付款', '同城闪送');
INSERT INTO `purchase_method` VALUES (9, 9, 4, '货到付款', '自提');
INSERT INTO `purchase_method` VALUES (10, 10, 8, '银行卡', '电子书');
INSERT INTO `purchase_method` VALUES (11, 11, 42, '微信支付', '同城闪送');
INSERT INTO `purchase_method` VALUES (12, 12, 6, '信用卡', '平邮');
INSERT INTO `purchase_method` VALUES (13, 13, 48, 'PayPal', '同城闪送');
INSERT INTO `purchase_method` VALUES (14, 14, 48, '银行卡', '快递');
INSERT INTO `purchase_method` VALUES (15, 15, 14, '货到付款', '同城闪送');
INSERT INTO `purchase_method` VALUES (16, 16, 18, '支付宝', '快递');
INSERT INTO `purchase_method` VALUES (17, 17, 35, '支付宝', '同城闪送');
INSERT INTO `purchase_method` VALUES (18, 18, 5, '货到付款', '自提');
INSERT INTO `purchase_method` VALUES (19, 19, 38, '微信支付', '平邮');
INSERT INTO `purchase_method` VALUES (20, 20, 48, '微信支付', '自提');
INSERT INTO `purchase_method` VALUES (21, 6, 37, '微信支付', '快递');
INSERT INTO `purchase_method` VALUES (23, 15, 27, '支付宝', '快递');
INSERT INTO `purchase_method` VALUES (24, 11, 33, '微信支付', '快递');
INSERT INTO `purchase_method` VALUES (25, 7, 23, '微信支付', '自提');
INSERT INTO `purchase_method` VALUES (26, 3, 41, '微信支付', '同城闪送');
INSERT INTO `purchase_method` VALUES (27, 20, 5, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (28, 5, 21, '银行卡', '平邮');
INSERT INTO `purchase_method` VALUES (29, 15, 48, '信用卡', '快递');
INSERT INTO `purchase_method` VALUES (30, 6, 41, '信用卡', '平邮');
INSERT INTO `purchase_method` VALUES (31, 13, 48, '信用卡', '自提');
INSERT INTO `purchase_method` VALUES (32, 8, 8, '微信支付', '电子书');
INSERT INTO `purchase_method` VALUES (33, 18, 16, '信用卡', '快递');
INSERT INTO `purchase_method` VALUES (34, 17, 39, 'PayPal', '自提');
INSERT INTO `purchase_method` VALUES (35, 1, 31, '信用卡', '电子书');
INSERT INTO `purchase_method` VALUES (36, 4, 43, '支付宝', '平邮');
INSERT INTO `purchase_method` VALUES (37, 7, 20, 'PayPal', '同城闪送');
INSERT INTO `purchase_method` VALUES (38, 12, 45, '支付宝', '自提');
INSERT INTO `purchase_method` VALUES (39, 6, 27, '银行卡', '平邮');
INSERT INTO `purchase_method` VALUES (40, 15, 28, 'PayPal', '电子书');
INSERT INTO `purchase_method` VALUES (41, 6, 31, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (42, 12, 11, '微信支付', '电子书');
INSERT INTO `purchase_method` VALUES (43, 5, 7, '信用卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (44, 10, 25, '货到付款', '快递');
INSERT INTO `purchase_method` VALUES (45, 18, 36, 'PayPal', '快递');
INSERT INTO `purchase_method` VALUES (46, 3, 11, '支付宝', '自提');
INSERT INTO `purchase_method` VALUES (47, 3, 47, '货到付款', '电子书');
INSERT INTO `purchase_method` VALUES (48, 20, 17, '信用卡', '平邮');
INSERT INTO `purchase_method` VALUES (49, 4, 36, 'PayPal', '同城闪送');
INSERT INTO `purchase_method` VALUES (50, 2, 2, 'PayPal', '平邮');
INSERT INTO `purchase_method` VALUES (51, 1, 39, '货到付款', '快递');
INSERT INTO `purchase_method` VALUES (52, 12, 12, '货到付款', '同城闪送');
INSERT INTO `purchase_method` VALUES (53, 11, 2, '微信支付', '电子书');
INSERT INTO `purchase_method` VALUES (54, 14, 28, '信用卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (55, 20, 33, 'PayPal', '电子书');
INSERT INTO `purchase_method` VALUES (56, 4, 45, '货到付款', '自提');
INSERT INTO `purchase_method` VALUES (57, 15, 49, '银行卡', '平邮');
INSERT INTO `purchase_method` VALUES (58, 20, 27, '信用卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (59, 4, 11, '支付宝', '平邮');
INSERT INTO `purchase_method` VALUES (60, 20, 18, '银行卡', '自提');
INSERT INTO `purchase_method` VALUES (61, 12, 29, '货到付款', '同城闪送');
INSERT INTO `purchase_method` VALUES (62, 17, 38, '微信支付', '快递');
INSERT INTO `purchase_method` VALUES (63, 5, 27, 'PayPal', '自提');
INSERT INTO `purchase_method` VALUES (64, 20, 5, '银行卡', '自提');
INSERT INTO `purchase_method` VALUES (65, 9, 24, 'PayPal', '自提');
INSERT INTO `purchase_method` VALUES (66, 6, 28, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (67, 17, 28, '银行卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (68, 19, 19, '信用卡', '自提');
INSERT INTO `purchase_method` VALUES (69, 17, 14, '银行卡', '快递');
INSERT INTO `purchase_method` VALUES (70, 7, 29, '银行卡', '平邮');
INSERT INTO `purchase_method` VALUES (71, 14, 31, '银行卡', '快递');
INSERT INTO `purchase_method` VALUES (72, 12, 22, '货到付款', '快递');
INSERT INTO `purchase_method` VALUES (73, 1, 46, 'PayPal', '电子书');
INSERT INTO `purchase_method` VALUES (74, 16, 31, '支付宝', '快递');
INSERT INTO `purchase_method` VALUES (75, 20, 11, '银行卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (76, 19, 24, '货到付款', '快递');
INSERT INTO `purchase_method` VALUES (77, 13, 34, '微信支付', '平邮');
INSERT INTO `purchase_method` VALUES (78, 13, 45, '支付宝', '自提');
INSERT INTO `purchase_method` VALUES (79, 12, 34, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (80, 18, 37, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (81, 20, 14, '货到付款', '电子书');
INSERT INTO `purchase_method` VALUES (82, 5, 34, 'PayPal', '快递');
INSERT INTO `purchase_method` VALUES (83, 11, 4, '微信支付', '自提');
INSERT INTO `purchase_method` VALUES (84, 19, 14, '微信支付', '自提');
INSERT INTO `purchase_method` VALUES (85, 14, 20, '银行卡', '快递');
INSERT INTO `purchase_method` VALUES (86, 2, 28, '货到付款', '快递');
INSERT INTO `purchase_method` VALUES (87, 20, 7, '银行卡', '自提');
INSERT INTO `purchase_method` VALUES (88, 14, 43, 'PayPal', '同城闪送');
INSERT INTO `purchase_method` VALUES (89, 19, 44, '货到付款', '自提');
INSERT INTO `purchase_method` VALUES (90, 13, 7, '信用卡', '电子书');
INSERT INTO `purchase_method` VALUES (91, 13, 43, 'PayPal', '同城闪送');
INSERT INTO `purchase_method` VALUES (92, 10, 48, '信用卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (93, 13, 24, '货到付款', '电子书');
INSERT INTO `purchase_method` VALUES (94, 14, 33, '银行卡', '同城闪送');
INSERT INTO `purchase_method` VALUES (95, 11, 4, '银行卡', '快递');
INSERT INTO `purchase_method` VALUES (96, 13, 26, '货到付款', '电子书');
INSERT INTO `purchase_method` VALUES (97, 14, 8, '银行卡', '电子书');
INSERT INTO `purchase_method` VALUES (98, 1, 34, '货到付款', '平邮');
INSERT INTO `purchase_method` VALUES (99, 16, 3, 'PayPal', '快递');
INSERT INTO `purchase_method` VALUES (100, 4, 5, '支付宝', '电子书');
INSERT INTO `purchase_method` VALUES (101, 11, 51, '微信支付', '平邮');

SET FOREIGN_KEY_CHECKS = 1;
