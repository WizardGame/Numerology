import tkinter as tk
from turtle import bgcolor

def main():
    InputFrame()

def InputFrame():

    TFroot = tk.Tk()
    TFroot.title('Thần số học')
    TFroot.geometry('600x200')
    TFroot.resizable(0,0)

    TFroot.rowconfigure(0,weight=1)
    TFroot.columnconfigure(0,weight=1)

    screen_width = TFroot.winfo_screenwidth()
    screen_height = TFroot.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (600/2))
    y_cordinate = int((screen_height/2) - (200/2))

    TFroot.geometry("{}x{}+{}+{}".format(600, 200, x_cordinate, y_cordinate))

    def myClick():
        valid = False
        name = inputNameField.get()
        day = ""; month = ""; year = ""
        try:
            day, month, year = inputBirthField.get().split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            if(day > 31 or month > 12 or day < 1 or month < 1 or year < 1):
                noti = tk.Label(inputFrame, text = "\nNgày sinh không hợp lệ", fg = "black", font = 16, bg="white")
                noti.grid(row=4,column=4)
                valid = False
            else:
                valid = True
        except Exception:
            noti = tk.Label(inputFrame, text = "\nNgày sinh không hợp lệ", fg = "black", font = 16, bg="white")
            noti.grid(row=4,column=4)
            valid = False
        if(valid):
            total1 = 0
            total2 = 0
            total3 = 0
            so_chu_dao = 0

            # Cộng ngày sinh thành 1 số
            if day >= 10:
                day_list = list(map(int, str(day)))
                for i in range(len(day_list)):
                    total1 += day_list[i]
            else:
                total1 = day

            # Cộng tháng sinh thành 1 số
            if month >= 10:
                month_list = list(map(int, str(month)))
                for i in range(len(month_list)):
                    total2 += month_list[i]
            else:
                total2 = month

            # Cộng năm sinh thành 1 số
            if year >= 10:
                year_list = list(map(int, str(year)))
                for i in range(len(year_list)):
                    total3 += year_list[i]
            else:
                total3 = year

            # Tìm số chủ đạo
            total = total1 + total2 + total3
            if total > 11:
                total_list = list(map(int, str(total)))
                for i in range(len(total_list)):
                    so_chu_dao +=  total_list[i]
            else:
                so_chu_dao = total
            TFroot.destroy()
            MainNumberFrame(so_chu_dao, total, name)

    inputFrame = tk.Frame(TFroot,bg="white")
    inputFrame.grid(row=0,column=0,sticky="nsew")
    lbuff = tk.Label(inputFrame, text = "                           \n\n", fg = "black", bg="white", font = 16)
    lbuff.grid(row=0,column=0)

    l1 = tk.Label(inputFrame, text = "Nhập họ và tên của bạn: ", fg = "black", bg="white", font = 16)
    l1.grid(row=1,column=3)
    l2 = tk.Label(inputFrame, text = "Nhập ngày sinh của bạn: ", fg = "black", bg="white", font = 16)
    l2.grid(row=2,column=3)

    inputNameField = tk.Entry(inputFrame, fg = "black", font = 16)
    inputNameField.grid(row=1,column=4)
    inputBirthField = tk.Entry(inputFrame, fg = "black", font = 16)
    inputBirthField.grid(row=2,column=4)
    enterButton = tk.Button(inputFrame, text = "Nhập", fg = "white", font = 16, bg="black", command = myClick)
    enterButton.grid(row=3,column=4)

    TFroot.mainloop()

def MainNumberFrame(so_chu_dao, total, name):

    def back():
        MNFroot.destroy()
        InputFrame()

    MNFroot = tk.Tk()
    MNFroot.title('Thần số học')
    MNFroot.geometry('800x250')
    MNFroot.resizable(0,0)

    MNFroot.rowconfigure(0,weight=1)
    MNFroot.columnconfigure(0,weight=1)

    screen_width = MNFroot.winfo_screenwidth()
    screen_height = MNFroot.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (800/2))
    y_cordinate = int((screen_height/2) - (250/2))

    MNFroot.geometry("{}x{}+{}+{}".format(800, 250, x_cordinate, y_cordinate))

    mnFrame = tk.Frame(MNFroot,bg="white")
    mnFrame.grid(row=0,column=0,sticky="nsew")

    backButton = tk.Button(mnFrame, text = "Quay lại", fg = "white", font = 16, bg="black", command = back)
    backButton.grid(row=10,column=1,sticky="S")

    if so_chu_dao == 2:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 2", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Đây là con số đặc biệt và rất hiếm, vì chỉ có duy nhất một số tổng 20 mới cho ra Con số chủ đạo 2."+
                                      "\nDo đó, trên thực tế những người có Con số chủ đạo 2 ít hơn hẳn so với những Con số chủ đạo khác."+
                                      "\nSố 2 nhìn chung là người nhạy cảm, khiêm tốn, đầy thiện chí giúp đỡ người khác.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 3:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 3", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Điểm nhấn của những người Số 3 là phần tư duy và lý luận."+
        "\nĐối với những người Số 3, đầu óc nhanh nhạy, tính hài hước và tư duy linh hoạt"+
        "\nnói chung giúp họ dễ dàng thành công trong công việc."+
        "\nNhưng khi sống kém tích cực, người Số 3 dễ để lại ấn tượng là người trịch thượng,"+
        "\ngia trưởng hoặc thích chỉ đạo người khác.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 4:
        if total == 22:
            l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 22/4", fg = "black", bg="white", font = 16)
            l1.grid(row=2,column=1)
            l2 = tk.Label(mnFrame, text = "Đây là con số đặc biệt, được trường phái Thần số học (Nhân số học) Pitago coi là “Con số vua”."+
            "\nNgười mang Con số chủ đạo 22/4 có tiềm năng gần như vô hạn"+
            "\nvà thường đạt được hầu hết những mục đích có vẻ bất khả thi.", fg = "black", bg="white", font = 16)
            l2.grid(row=4,column=1)
            l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
            l3.grid(row=3,column=1)
            l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
            l4.grid(row=1,column=1)
        else:
            l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 4", fg = "black", bg="white", font = 16)
            l1.grid(row=2,column=1)
            l2 = tk.Label(mnFrame, text = "Người Số 4 có thiên hướng về “thực tế” hoặc “ thực hành” -"+
            "\nhọ thích bắt tay vào việc hơn là ngồi bàn luận về các giá trị việc đó mang lại."+
            "\nChính sự thực tế này giúp những người Số 4 luôn tiến về phía trước."+
            "\nHọ thuộc nhóm những người nguyên tắc và đáng tin cậy nhất."+
            "\nNgười Số 4 thường chìm đắm trong công việc và xao lãng những việc mang đến sự cân bằng cho cuộc sống của họ,"+
            "\nđặc biệt là cuộc sống gia đình.", fg = "black", bg="white", font = 16)
            l2.grid(row=4,column=1)
            l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
            l3.grid(row=3,column=1)
            l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
            l4.grid(row=1,column=1)
    elif so_chu_dao == 5:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 5", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Người có Con số chủ đạo là 5 thường có khuynh hướng cố gắng thoát khỏi sự trói buộc,"+
        "\nthường nhạy cảm và có nhu cầu bày tỏ cảm xúc."+
        "\nPhần lớn người Số 5 cảm thấy khó làm việc theo giờ giấc quy định nghiêm ngặt."+
        "\nHọ có trực giác rất tốt, với cảm xúc sâu sắc và tư duy nghệ thuật mạnh mẽ.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 6:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 6", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Chúng ta sẽ thấy người Số 6 ưu tú trong rất nhiều lĩnh vực sáng tạo, từ ở nhà cho đến đấu trường quốc tế."+
                                      "\nHọ mang một trọng trách lớn trong cuộc sống, thứ đòi hỏi ở họ sự tận tâm sâu sắc."+
                                      "\nTất cả những người Số 6 đều có khả năng thiên phú này, nhưng họ thường bị gánh nặng trách nhiệm làm cho"+
                                      "\nbất an và lo lắng,từ đó mắc kẹt trong áp lực căng thẳng.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 7:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 7", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Một trong những đặc điểm độc đáo ở những người Số 7 là họ được học hỏi theo cách riêng của mình."+
        "\nKhông dừng lại ở việc tiếp nhận các chỉ dẫn tối thiểu từ người khác, "+
        "\nngười Số 7 khát khao được học bằng cách tự trải nghiệm."+
        "\nChính vì điều này, người Số 7 thường phải hy sinh ít nhất một trong ba khía cạnh của cuộc sống:"+
        "\nsức khỏe, tình yêu, tiền tài.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 8:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 8", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Những người mang Số 8 chủ đạo là những người coi sự độc lập là một trong những yếu tố quan trọng hàng đầu "+
        "\ntrong cuộc sống. Họ có thể là những người khá phức tạp, sở hữu cá tính mạnh, sức mạnh và trí tuệ hơn"+
        "\nngười. Nhưng về khả năng biểu đạt lòng biết ơn và sự trân trọng thì người Số 8 cảm thấy rất khó thể hiện.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 9:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 9", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "So với những nhóm khác, người mang Con số chủ đạo 9 sẽ nhân gấp ba lần yếu tố: hoài bão, trách nhiệm và lý"+
                                    "\ntưởng. Họ luôn đặt yếu tố con người lên hàng đầu.Người Số 9 luôn tự cảm thấy mình đầy trách nhiệm."+
                                    "\nHọ phù hợp với nghệ thuật và các lĩnh vực nhân văn hơn là với khoa học hay thương mại.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 10:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 10", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Cuộc sống của người Số 10 có hai đặc điểm nổi trội: khả năng thích nghi và khả năng thay đổi."+
                                    "\nTính linh hoạt của họ có thể hỗ trợ người khác rất nhiều trong việc thích ứng với các thay đổi trong cuộc"+
                                    "\nsống.Khi sống tích cực, họ có thể là người rất quảng giao, được yêu thích; nhưng khi sống tiêu cực,"+
                                    "\nhọ có thể là những cá nhân lạc lối, bất an và lao đao trên đường đời.", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)
    elif so_chu_dao == 11:
        l1 = tk.Label(mnFrame, text = "Số chủ đạo của bạn là 11", fg = "black", bg="white", font = 16)
        l1.grid(row=2,column=1)
        l2 = tk.Label(mnFrame, text = "Con số chủ đạo 11 có một trường năng lượng tâm linh đặc biệt mạnh mẽ, "+
                                     "\ngiúp những người mang Con số chủ đạo này có tiềm năng phi thường để phát triển nhận thức ở Thể Siêu thức. "+
                                    "\nĐáng tiếc là phần lớn những người Số 11 lại không đủ khả năng phát huy tiềm năng đó. ", fg = "black", bg="white", font = 16)
        l2.grid(row=4,column=1)
        l3 = tk.Label(mnFrame, text = "**************", fg = "white", bg="white", font = 16)
        l3.grid(row=3,column=1)
        l4 = tk.Label(mnFrame, text = "Tên: "+name, fg = "black", bg="white", font = 16)
        l4.grid(row=1,column=1)

    MNFroot.mainloop()

main()