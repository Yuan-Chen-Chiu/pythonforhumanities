期末專案構想：今晚誰來當家
===================

## 目的/功能說明（約500字即可）
2018年台北市長選情激烈，些微票數就可翻轉局面。從中選會公布之台北市行政區得票數來看，可知某些區域候選人色彩較濃厚，在開到特定區域的票倉時，也會看到PTT上鄉民哀鴻遍野或驚喜連連。
本遊戲將由你來選擇自己的隊友，一共有3次機會，可以選擇3個行政區的區民和你組隊；同樣的，系統也會派出3個行政區的對手與你抗衡。系統介面簡述如下：
== 請選擇你支持的候選人(柯文哲/丁守中)：    ##因為其他候選人票數懸殊過大，故暫不列入考慮

== 第一回合：
1.請選擇你要選擇的行政區(中正、大同、中山、松山、大安、萬華、信義、士林、北投、內湖、南港、文山)：

系統將派出另一個行政區與你抗衡，並計算出票數與比率差距。

在重複3回合之後(票數為累加)，將計算出最終贏家，勝負判斷方式為總票數或以比例計算。
## 你覺得可能會遇到的困難，請盡量清楚地條列敘述。
1. 除了系統隨機分派對手外，也可以改成真人實戰，由另外一個人選擇里與其抗衡。
2. 怕以里為單位是否要整理的資料會太多，但以行政區又太容易。
3. 回合數(3回合)是否太少。

## 如何達成此專案的功能
1. 介面互動

    使用者將以文字介面和程式互動。程式的輸入使用input()函式、輸出則用print()函式。所有的使用者輸入都會有程式提示既定選項，故僅需非常少量的（或不需要）語句剖析。

2. 資料處理與彙總

    每回合使用者所選擇的行政區不得相同，因此要import random並利用random.shuffle讓系統隨機選擇的行政區不會和前一次相同。


3. 格式化輸出

    在專案初期僅提供一般文字介面的輸出回饋，所有的文字顯示都使用內建的print()即可完成。