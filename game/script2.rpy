label chess0:    
    define m = Character('【伊森】')
    define l = Character('【莉兹】')
    define i = Character('【伊莎贝拉】', color="#c8ffc8")

    '大概是我们又聊到了沉重的话题，三个人都沉默了下来。'
    '又是一阵直升机从我们头顶急掠而过的引擎声。屋外的广播再次响了起来。'
    '……宵禁时段请遵守法律规定，待在家中，防止病毒蔓延……'
    '一直在一旁默默地着看着我和贝拉谈天的莉兹，这时突然开了口。'
    show liz normal 23
    l '贝拉，你还能来看我，我真的很感激。'
    show isa normal 22
    i '哎？怎么突然说起这种话。我们是那么多年的朋友了，当然要来看你啊。'
    show liz normal 22
    l '最近几个月，我越来越不想打开我的手机，倒不是因为时常的断电断网……'
    show liz normal 24
    l '只是因为通讯录里，同学和朋友们的手机号……已经有一大半，永远也打不通了。'
    show liz normal 25a
    l '每天晚上我都要在自己的床上躺到半夜才能睡着，我害怕如果有一天连贝拉你也联系不上了，我该怎么办……'
    m '莉兹……'
    show liz normal 53
    l '对不起，本来我今天已经下了决心，不提起这些……但是一见到你的时候，我心里的焦虑就开始像疯了一样地蔓延……'
    show liz normal 53a
    l '我害怕有一天，会不会连你也……'
    show isa normal 04
    i '好啦，至少现在你不用担心了。'
    '她向莉兹摇了摇手腕，给她看上面的手环。'
    i 'Your best friend is always here. This bracelet... is a proof that I will not leave you. Ever. '
    show liz normal 21
    l '嗯……谢谢你，贝拉。'

    show isa normal 02
    i '莉兹，你的腿现在恢复得怎么样了？'
    show liz normal 21
    l '一直都有进展，只是比较慢就是了。我现在还是可以站起来走几步不至于摔倒，但是大部分时间还是得坐在轮椅上……'
    show isa normal 11
    i '那我就放心了！只要每天保证进行一定量的康复运动，你的腿一定会慢慢好起来的。'
    '莉兹则是信心十足地点了点头。'
    show liz normal 02
    l '嗯，我也会努力的。不能一直在轮椅上坐着，那样只会给哥哥添麻烦。'
    show isa normal 43
    i '不许说那样的话！莉兹，你才不是麻烦，不管是对我还是对伊森来说。'
    show isa normal 31
    i 'You are just having a rough time.'
    '伊莎贝拉给我使了个眼色，不用说我也明白她的意思。'
    m '贝拉说的没错。'
    show isa normal 53
    i '而且，如果你出了什么意外……莉兹，我真的不知道还有什么能支撑我生活下去了。'
    show isa normal 52
    i '一切都会好起来的，放心吧。'
    show liz normal 51
    l '我明白。谢谢你，贝拉。'

    '我看着莉兹脸上的笑容，心中突然也多了一点希望。'
    '是啊，也许……真的会有奇迹吧。'
    '当然，只有我和伊莎贝拉两人真的阅读过莉兹病例上，医生的诊断。'
    '病毒带来的后遗症，是永久性的神经损伤，康复的可能性是完完全全的零。'
    '莉兹今后的一生，可能都没有办法正常地走路了，只是我们没有让她知道罢了。'
    '……'
    '但是，食物缺乏也好，犯罪猖獗也好……至少我们还能活着。'
    '即使是只剩下我们两个人的家，也能平平安安地熬过这场灾难……'

    show isa normal 02
    i '哦对了。'
    i '我今天来的时候，带了些好玩的东西过来，希望可以帮我们打发些无聊时间……'
    show isa normal 22
    i '要不是现在市区北边这块网络几乎瘫痪，我宁可躺在沙发上玩几局游戏。'
    show isa normal 02
    i '我今天带了一盒国际象棋，还有一盒UNO牌。'
    m '喔！听起来挺有趣的。'
    show isa normal 11
    i '莉兹和我在高中的时候可是学校里象棋社团的顶尖选手呢，伊森，你呢？'
    m '国际象棋吗……虽然我并不是很会玩，莉兹对此倒是很有研究。'
    m '她一定常常和你一起对弈吧。'
    show isa normal 04
    i 'UNO呢？'
    m '适合全家一起玩的卡牌游戏，我偶尔玩过几局。'
    show isa normal 02
    i '那，你们来选吧。莉兹，你想玩什么？'
    show liz normal 01
    l '让哥哥选吧，要是象棋的话，今天我想看哥哥和伊莎贝拉下一局。'
    show isa normal 04
    i '噢！原来如此，莉兹这次想做一回解说了啊。'
    $ uno_choice = False
    
    menu:

        i '没问题！那伊森你来选。……我和你下几盘棋，或者我们三个可以来打几轮UNO。'

        "下棋":
            jump chess

        "UNO":
            $ uno_choice = True
            jump uno
               
label chess:
    show isa normal 42
    i '很好，看来你已经做好觉悟了，伊森。'
    show isa normal 44
    i '准备好受苦吧！'
    jump start_2

label uno:
    show isa normal 44
    i '哼哼……！很遗憾，我没有带Uno牌！所以只剩象棋了！'
    m '所以你一开始就不要给这个选项啊……'
    show isa normal 12
    i '好了好了，人生就是要有惊喜才精彩嘛！'
    m '这个……'
    '我面露难色地看向莉兹，而她则是一脸期待地看着我。'
    '贝拉就是这样的女孩啦……她的眼睛似乎在这样告诉我。'
    jump start_2

label start_2:
    show isa normal 02
    i '那么，你选哪方？'
    m '……'

    menu: 
        '先手白棋':
            jump start_3w
        '后手黑棋':
            jump start_3b

        '这回我总算有的选了吗？' if uno_choice:
            jump start_3a

label start_3w:
    m '白方。'

    jump start_3

label start_3b:
    m '黑方。'

    jump start_3

label start_3a:

    m '这次你真的把两种颜色的棋子都带来了，对吧？'
    show isa normal 12
    i '哈哈哈哈！伊森，你可真幽默。'
    jump start_3

label start_3:

    '伊莎贝拉的技术出人意料地好，我的阵线在她的攻势下，十个回合就彻底溃败了。'
    show isa normal 44
    i '将军。'
    m '这……这……'
    '伊莎贝拉的攻击毫无死角，我手中的国王已经无路可走。万般无奈之下，我摆手认输，在沙发上瘫坐下来。'
    '果然，无论先手后手怎么选，我都不是伊莎贝拉的对手。'
    m '技不如人。我输了。'
    show liz normal 12
    l '啊哈哈……我都没来得及解说几句，哥哥怎么就输了啊……'
    m '没有办法，我平常不怎么下棋。'
    show isa normal 02
    i '想要再来一局吗？'
    m '实力差距也太大了，像我这样总是眨眼间就被你将死的话，两个人都没什么游戏体验啊。'
    m '要不，还是让莉兹来吧。我觉得旁观高手之间的对弈会更有意思一点。'
    show liz normal 23
    l '啊，我吗？可以倒是可以，但……'
    m '莉兹你也不想一直看到哥哥被暴打对吧？来，替我报仇吧！'
    show liz normal 01
    l '那好吧，我就不客气了……'
    '莉兹推着自己的轮椅，挪到了棋盘前面。而伊莎贝拉趁这时间已经摆好了棋盘。'
    show isa normal 02
    i '莉兹，你还记得我们上次面对面下棋是什么时候吗？'
    show liz normal 51
    l '记不太清楚了，可能……已经是去年的事了吧。'
    show isa normal 04
    i '我还记得哦。那还是去年的一月底，疫情爆发之前，大家的生活还一切正常的时候。我们在学校二楼的活动室里下了暑假前的最后一盘棋，莉兹你以微弱的优势获胜。'
    show isa normal 53
    i '然后就是ARX病毒的爆发，学校全部关闭，一律改成网上授课……咱们就再也没有面对面对决过了。'
    show isa normal 42
    i '我可是很记仇的哦，我输掉的，总有一天会赢回来。'
    show liz normal 12
    l '这样啊，贝拉你这段时间一定努力钻研了不少下棋的技巧吧，我可能都打不过你了呢。'
    show isa normal 44
    i '哼哼，那就拿出点你的真本事吧！莉兹·塞弗兰小姐！'
    '伊莎贝拉率先出手,推进士兵。而莉兹也拿起了自己的棋子，似乎正在思考着什么。'
    '然而她好久都没有做出决定，抓着棋子的手也在半空中停滞，迟迟没有放下。'
    show isa normal 01
    i '莉兹？'
    '茶几上传来清脆的摔落声，莉兹的手似乎失去了力气，手中的棋子掉在了桌上。她的身体摇摇欲坠，我眼疾手快，冲到她的面前扶住了她的身子。'
    m '莉兹！你怎么了？'
    show isa normal 21
    i '莉兹？！'
    '然而莉兹没有回答我们中的任何一个，她的眼神涣散，而身体却像断了线的木偶一般脱力。突然间，她用双手捂住了嘴，剧烈地咳嗽了起来。'
    '我过去扶住她的背，试图让她的咳嗽平静下来，然而完全派不上用场。'
    '伊莎贝拉被莉兹突然的状况弄得手足无措，只能在一旁紧张地观望着她。直到半分钟过后，莉兹才止住了咳嗽，她低下头来捂着胸口，试图让呼吸平缓下来。'
    show liz normal 25a
    l '哥哥……抱歉。我只是……突然觉得有些不舒服。'
    '她抬起头看着我，眼神中只有歉意。'
    m '……莉兹，你已经没事了吧？'
    show isa normal 21
    i '莉兹，你差点要吓死我了。这到底是怎么回事？'
    m '我不知道……我也从来没见过莉兹这样子咳嗽过。'
    show liz normal 21
    l '我没事，不用担心我……大概只是呼吸进了什么灰尘吧，最近家里的空气质量不太好呢，嘿嘿……'
    '莉兹笑了笑，只是笑得十分勉强。'
    show liz normal 22
    l '最近除了咳嗽，也稍微有点发烧，有时候还会身体疲软，使不上力气……'
    l '大概是被流感缠上了吧……现在正是秋天，天气变凉的时候。'
    m '嗯，肯定是的，不要多想。'
    '我从客厅的衣架上拿起一块毛毯，盖在莉兹的肩上，将她的身体裹住。'
    m '现在应该好点了吧？'
    show liz normal 23
    l '嗯，只是有些气短，说话说多了就会稍微头晕……不过没什么关系。话说回来，我还有棋局没下完呢，对吧？'
    show isa normal 23
    i '莉兹……'
    show isa normal 21
    i '你确定你还能继续吗？我看你好像有点虚弱了……我只是很担心你。'
    show liz normal 21
    l '啊，我确实是想休息一下，下棋太费脑子啦……'
    show isa normal 02
    i '不要紧。莉兹你在这儿躺一会儿吧，要喝点什么吗？'
    show liz normal 01
    l '谢谢你贝拉，但是不用，我不渴。'
    show isa normal 24
    i '那……我和伊森再下一盘棋，你在旁边看着，怎么样？'
    show liz normal 01
    l '嗯，好的。'
    '我接过莉兹落在棋盘上的那颗士兵，看看伊莎贝拉，又看看莉兹，最后落了子。'
    '伊莎贝拉也是一样，看看我，又看看莉兹，下出了第二步。'
    '我们两个都没有说话，似乎达成了一种奇怪的默契。我们其实好像都在下棋，但其实注意力都放在莉兹的身上。'
    '而莉兹好像也没有再有什么身体不适的迹象，专心地盯着我们的对弈。'
    '也许刚刚只是偶然的空气质量问题吧……就像莉兹说的那样。'
    '已经没有什么ARX病毒了，莉兹已经痊愈……没有什么病可以再伤害到她。我这样对自己说着，努力让自己的注意力集中到眼前的棋盘上。'
    '……'
    show isa normal 01
    i '将军。'
    '伊莎贝拉轻声说出了象征游戏结束的两个字，我又一次倒在了她凌厉的攻势下。无论是控场，棋路，还是随机应变的能力，我都差她太远。'
    m '太难了，真是太难了……想要赢下贝拉你，果然还得要十年吧……'
    show isa normal 51
    i '伊森……你看。'
    '而伊莎贝拉则是用眼神指示我看看一旁的莉兹。'
    '我才一小会儿没有去看她，莉兹居然就已经躺在轮椅上安静地睡着了。她的呼吸平稳而均匀，下午的阳光照在她的脸上，给她有些苍白的面容上添上了些暖色。'
    '希望她正在睡个好觉。'
    '我怕莉兹着凉，于是起身走到从客厅的衣架前面，从那里拿了一条毛毯下来，盖到她的身上。'
    show isa normal 54
    i '你真是个温柔的男人呢，伊森。'
    show isa normal 04
    i '要是你一直像这样下去的话，也许有一天我会爱上你哦。'

    menu:
        '别拿我开玩笑了……':
            jump start_4a

        '只要那时候我还活着……':
            jump start_4b

label start_4a:

    m '别拿我开玩笑了，艾德勒小姐……'
    show isa normal 24
    i '啊哈哈，开个玩笑也不行吗？真是个无趣的人……'
    jump start_4

label start_4b:
    m '可以啊，要是等到那一天我还没被ARX病毒弄死，那你就嫁给我吧。'
    show isa normal 01
    i '……！！'
    '伊莎贝拉似乎完全没有预料到我这句话，一下子涨红了脸，假模假样地清了清嗓子。'
    show isa normal 04
    i '咳咳！那你可得好好照顾好自己啊，可别让我的一厢情愿落了空！'
    jump start_4

label start_4:
    '我没有再理会伊莎贝拉，因为我感觉莉兹身上有些不对劲的地方。有一丝疑虑从我的心底里升起，我却说不出来到底是为什么。'
    '莉兹……是不是在隐瞒着什么东西？'
    '我掀开盖在她身上的毛毯，看见莉兹还是牢牢地把左手攥紧，靠在胸前，从那会儿刚咳嗽开始就没挪动过位置。'
    '她的手里是握着什么东西吗？好像刚刚一直都是这样，我却一直都没发现……'
    '也许是十几年来兄妹血缘带来的直觉，我不由自主地伸出手去，翻开了莉兹的手掌，里面的景象却让我后背如浸入了冰水一般寒冷。'
    '是血……凝固的血迹。'
    show isa normal 31
    i '伊森，发生什么事了？'
    '伊莎贝拉把目光凑过来，看到了莉兹手掌上的血迹。'
    show isa normal 21
    i '这……这是……'
    m '也许是刚刚咳嗽的时候咳出来的。'
    show isa normal 23
    i '咳血，还有她之前说的发烧，乏力……天啊，这不可能……'
    i '这，这不又是感染ARX的症状了吗？'
    m '我……我也不知道！不行，我得赶紧把她送去医院，让医生来看看！'
    '我像是疯了一般地站起身来，想找件大衣来披上。伊莎贝拉在我背后说的一句话，却仿佛当头一盆冷水浇下。'
    show isa normal 33
    i '伊森，你冷静一点。'
    show isa normal 31
    i '你现在出门，能找到谁来帮你呢？现在疫情的严重程度，早就不是年初时候可以相比的了。'
    show isa normal 21
    i '你可能并不了解，整个城区的医疗力量，已经被ARX毁得差不多只剩下了一两成。两个月前，还幸存的医生和护士就都被政府集中转移到了市中心的西诺山医院里。'
    show isa normal 33
    i '现在整个奥伦市区，只剩下那一座医院了。你要怎么绕开军队的封锁，进入到市中心？'
    show isa normal 31
    i '而且，以西诺山医院现在极为有限的医疗资源，只会去优先救治被感染的军队士兵和政府的高官要员。你觉得没有身份的平民，能得到那样的待遇吗？'
    m '所以我们这些平民就只能在家里等死是吗？！'
    show isa normal 23
    i '……'
    show isa normal 21
    i '我倒是希望附近还有能巡诊的家庭医生，但是……恐怕也很难联系到。我们家附近街区的那位艾什莉医生，几个月前也病死了……'
    m '那群混账……'
    '莉兹还躺在自己的轮椅上熟睡着，没有被我们两个的争执吵醒。'
    '我看着她略显憔悴的脸，难以名状的绝望感缓缓攀上了我的脊背。我攥紧了双拳，却一句话也说不出来。'
    '伊莎贝拉一声不响地走了过来，把自己的手轻放在我的拳头上。她手掌上传来的温暖也让我的心情慢慢地平复了下来。'
    show isa normal 53
    i '……'
    '一定还有别的办法的，不是吗。我这么对自己说着。'
    show isa normal 03
    i '听着，伊森，我还认识一个人。也许她不是什么有经验的医生，但是如果莉兹的症状和ARX有着什么关联的话，她也许能帮得上什么忙……'
    '伊莎贝拉从衣兜的钱包里抽出了一张名片。'
    show isa normal 01
    i '去联系名片上的这个人，她……是UBL里的一位研究员，来自日本的病毒学家。我几星期前去那里做免疫检测的时候，见过她一面，就和她稍微聊了几句……'
    show isa normal 23
    i '看她有些眼熟，只是又没来得及多问。但是我有听其他的研究人员提起过，如果从ARX病痊愈的人，突然又出现和染病一开始相似的症状，那说明一定是有什么问题了……'


    '我接过那张名片，上面是UBL研究所的烫金徽章，下面是那个人的名字，用工整的英文拼写出来的\“YUKI\”。头衔是首席研究员。'
    '我的心脏不由自主地紧缩了一下。'
    '果然……是她。'
    show isa normal 21
    i '伊森？你看起来不太对劲。'
    m '……没事。'
    '我平淡地回答了一句，把名片收进衣服的口袋。'
    m '真的是帮了大忙了，贝拉。谢谢你。我一会就去联系上面的人。'
    '伊莎贝拉点了点头。'
    show isa normal 53
    i '莉兹她，最近还有什么别的症状吗？'
    m '最近确实咳嗽地更频繁了，好像有什么东西在一点一点地抽走她的力气。今天咳出血来，还是头一次……'
    m '我们两人每天的三餐，我都是尽量让营养搭配均衡，尽一切可能利用上储备不多的食物。但是似乎没有什么用。'
    '伊莎贝拉看着我，用一个心情复杂的微笑回应了我。'
    show isa normal 32
    i '谢谢你所做的一切……当然，大部分是替莉兹谢的。'
    show isa normal 34
    i '这段时间，辛苦你了。I know youve had a tough time.'
    '她看了看窗外，天色已经越来越暗了，大概是已经到了日落时分。'
    show isa normal 01
    i '啊，马上就要天黑了呢。'
    m '贝拉，你这就要走了吗？'
    show isa normal 03
    i '快到宵禁的时间了，到时候想要绕开军队的巡逻会浪费更多时间。'
    m '那……莉兹还在睡着，要不要我叫醒……'
    show isa normal 02
    i '不用了，让她好好睡一觉吧。'
    '伊莎贝拉站了起来整理了一下自己的衣服。'
    m '你准备怎么回去？'
    show isa normal 04
    i '和我来的时候一样，维克托开车来接我，他已经在外面等着了。'
    m '嗯，想想也是……时间也是掐的正好。'