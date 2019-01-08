期末專案構想：臺北市今晚誰來當家
===================

## 專案公開資訊

### 專案題目（格式：程式名稱/專案題目，30中文字以內，2個英文字母算1個中文字）
臺北市今晚誰來當家

### 簡述（100字內）
今晚誰來當家是一個簡易計算臺北市主要兩位市長候選人(丁守中、柯文哲)於各行政區的得票數，並加上簡易互動式比賽，讓使用者更感受開票時票數差距的臨場感。

---

## 目的/功能說明（約500字即可）
2018年台北市長選情激烈，些微票數就可翻轉局面。從中選會公布之台北市行政區得票數來看，可知某些區域候選人色彩較濃厚，在開到特定區域的票倉時，也會看到PTT上鄉民哀鴻遍野或驚喜連連。
本遊戲將由你來選擇自己的隊友，一共有3次機會，可以選擇3個行政區的市民和你組隊；同樣的，系統也會派出3個行政區的對手與你抗衡。系統介面簡述如下：
== 請選擇你支持的候選人(柯文哲/丁守中)：    ##因為其他候選人票數懸殊過大，故暫不列入考慮

== 第一回合：
1.請選擇你要選擇的行政區(中正、大同、中山、松山、大安、萬華、信義、士林、北投、內湖、南港、文山)：

系統將派出轄下另一個行政區與你抗衡，並計算出票數與比率差距。

在重複3回合之後(票數為累加)，將計算出最終贏家，勝負判斷方式為總票數或以比例計算。

## 你覺得可能會遇到的困難，請盡量清楚地條列敘述。
1. 除了系統隨機分派對手外，也可以改成真人實戰，由另外一個人選擇行政區與其抗衡。
2. 原本構思是以里為單位與對手抗衡，但資料過多難以整理，故先以行政區為單位。
3. 回合數(3回合)是否太少

## 如何達成此專案的功能
1. 介面互動

    使用者將以文字介面和程式互動。程式的輸入使用input()函式、輸出則用print()函式。所有的使用者輸入都會有程式提示既定選項，故僅需非常少量的（或不需要）語句剖析。

2. random.shuffle
    
    每回合使用者所選擇的行政區不得相同，因此要import random並利用random.shuffle讓系統隨機選擇的行政區不會和前一次相同。

3. 資料處理與彙總
    
    因共有三回合對決，且最後勝負是三回合票數加總與總比例計算，因此可以迴圈走過使用者所儲存的里票數，記錄到相對應的暫存變項，並在每次迭代中對該暫存變項的值做加總計算。

4. 格式化輸出

    在專案初期僅提供一般文字介面的輸出回饋，所有的文字顯示都使用內建的print()即可完成。

## 實作時間表

### W14 12/12  Checkpoint 1

* 寫出使用者介面
  寫出使用者輸入的介面，一開始先呈現主頁面，並區分為輸入丁守中"ding_vote_sum()"與柯文哲"KP_vote_sum()"兩種input途徑。
  將柯文哲和丁守中在各行政區的票數以dict方式呈現。

### W15 12/19  Checkpoint 2

* 完成ding_vote_sum()與KP_vote_sum()
  完成丁守中與柯文哲的計票方式，計算每次的得票數。

### W16 12/26  Checkpoint 3

* 完成count_round計算每局得票數，以及final_count計算最終贏家與得票數。

## W17 01/02  口頭報告 / beta release

* 測試程式功能

* 調整其他程式小問題

## 未來開發計畫

* 考慮以里為單位，而非行政區。

* 可擴展到其他縣市，或全國範圍的總統大選或公投等。

