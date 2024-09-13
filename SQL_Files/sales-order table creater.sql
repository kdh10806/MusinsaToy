-- 더미 데이터 : Test - SalesOrder - ServiceTest 돌리기

drop table IF EXISTS `sales_order_product_option`;
drop table IF EXISTS `sales_order_product`;
drop table IF EXISTS `SALES_ORDER_detail`;
drop table IF EXISTS `SALES_ORDER`;

-- 주문
CREATE TABLE `SALES_ORDER` (
   `ORDER_ID`   VARCHAR(30)   NOT NULL,
   `member_id`   INT   NOT NULL,
   `ORDER_DATETIME`   DATETIME   NOT NULL,
   `STATE_CODE`   tinyint   NOT NULL,
   `RECIPIENT`   VARCHAR(30)   NOT NULL,
   `PHONE`   VARCHAR(15)   NOT NULL,
   `ADDRESS_A`   VARCHAR(80)   NOT NULL,
   `ADDRESS_B`   VARCHAR(80)   NOT NULL,
   `POSTCODE`   VARCHAR(5)   NOT NULL,
   `DELIVERY_REQUEST`   VARCHAR(80)   NOT NULL,
   `PAYMENT_ID`   BIGINT   NOT NULL,
   `PAYMENT_METHOD`   VARCHAR(15)   NOT NULL,
   `PAYMENT_AMOUNT`   INT   NOT NULL
);
ALTER TABLE `SALES_ORDER` ADD CONSTRAINT `PK_SALES_ORDER` PRIMARY KEY (
   `ORDER_ID`,
   `member_id`
);

-- 주문한 상품
CREATE TABLE `SALES_ORDER_PRODUCT` (
   `ORDER_ID`   VARCHAR(30)   NOT NULL,
   `PRODUCT_ID`   VARCHAR(25)   NOT NULL,
   `PRICE`      int   NOT NULL,
   `AMOUNT`   int   NOT NULL,
    
    CONSTRAINT PK_SALES_ORDER_PRODUCT  
      PRIMARY KEY (`ORDER_ID`,`product_id`),
    CONSTRAINT FK_SALES_ORDER_TO_SALES_ORDER_PRODUCT 
      FOREIGN KEY (`ORDER_ID`)
      REFERENCES `SALES_ORDER` (`ORDER_ID`),
    CONSTRAINT `FK_product_TO_SALES_ORDER_PRODUCT_1` 
      FOREIGN KEY (`product_id`)
      REFERENCES `product` (`product_id`)
);


-- 주문한 상품의 옵션
CREATE TABLE `SALES_ORDER_PRODUCT_OPTION` (
   `option_pk` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   `order_id`   VARCHAR(30)   NOT NULL,
   `product_id`   VARCHAR(25)   NOT NULL,
   `option_id`   VARCHAR(10)   NOT NULL,
   `option_category`   VARCHAR(10)   NOT NULL,
   `option_name`   VARCHAR(10)   NOT NULL,
   `option_depth`   VARCHAR(10)   NOT NULL,
   
   CONSTRAINT FK_SALES_ORDER_PRODUCT_TO_SALES_ORDER_PRODUCT_OPTION_1
      FOREIGN KEY (`product_id`, `order_id`)
      REFERENCES `SALES_ORDER_PRODUCT` (`product_id`, `order_id`),

   INDEX idx_order_product (`order_id`, `product_id`)
);

