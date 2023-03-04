# Inventory-system-implementation
I implement an inventory system on AWS cloud using PostgreSQL engine.
## Operations
There are four main types of actions in this system. First is about the distribution, second is about sales, third is about the clothes and sale look-up, forth is about the static.
### Distribution Part
1. Add
This function is to add the number of clothes in the distribution. It will be called as two condition. 1.new clothes. 2. more old clothes. The difference between these two is that we need to use insert for new clothes instead of update and the new clothes will be all stored in the office initially.
2. Deliver
The work flow of clothes distribution is that the merchandises will be stored in the office initially and be delivered to the stores later. Occasionally, the clothes need to be delivered between stores. This function can deal with the both scenario. When we want to deliver a clothes from store1 to store2, we need to subtract the number of transfers from store 1 and increase the number of transfers from store 2
3. Import
When we first import a clothe, we need to construct the information of a clothe in the relation of clothes.However, we need to update the number of clothes using the function add with the input argument new = True.
4. Decrease
Sometime, the clothes might be stolen or have some deficient so it can’t be sold. In this case, we need directly decrease the number of clothes in the distribution.

### Sale Part
1. Sold
When we sell a clothe, we need to do two queries. 1. Insert a record in the relation of sales. 2. Decrease the number of clothes being sold in the relation of distribution. Moreover, we need to get the time when clothes are sold using the datetime module. As you can see, I will record the current time 20 minutes ago and take the whole number as the time to sell clothes, this is because the time in the weather relaton is the foreign key for this time, and the weather relation update rate has a 15-minute delay, and are integers. Moreover, because the sales might give the costumer some unique discount, so we keep the input argument income for them the set the final sold price.
2. Exchange
Sometime, costumer will bring their clothes back to exchange for another clothes. In this case we need to insert a exchange record. For this record, we need to find the date of clothes being sold.

### Look-up Part
1. Number
To get the number of a cloth for all color and corresponding size.
2. Size and Color chart
To get the color and size chart for a clothe.
3. detail
To get the complete information of clothes in the clothes relation.

### Static Part
1. Sales Volume
There are three types of sales volume. 1. Daily 2. Monthly 3. Year. For the daily report, we need to give the specific date in the format of {YYYY-MM-DD}. For the monthly report, we need the format of {YYYY-MM}. For the year, we need the format of {YYYY}. The report will be first classified with store name and then the sales.

## Lambda function on AWS
I fetch the weather data on CWB and store them in system automatically using AWS Lambda function. The CWB provide a useful [api tool](https://opendata.cwb.gov.tw/dist/opendata-swagger.html) so that we can download the latest weather date via URL. So I use python module request to get the json file via URL provided by api, and then automatically update the newest data through AWS lambda function every ten minutes from 10am to 10pm every day. To do so, I use CloudWatch event as the trigger (the expression: cron(0/10 2-18 * * ? *)).
