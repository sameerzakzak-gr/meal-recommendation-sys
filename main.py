import PIL

from Rounded import RoundedButton
from experta import *
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
# from Engine import FOODIE, time_cooking, weather, Tim, components, diseases


from Rounded import RoundedButton
from experta import *
from tkinter import *
import xlrd

class cooking(Fact):
    pass
class components(Fact):
    pass
class diseases(Fact):
    pass
class weather(Fact):
    pass
class time_cooking(Fact):
    pass

Tim = 0
class FOODIE(KnowledgeEngine):
    j = 2
    t = 6
    dis = []
    comp = []
    wb = xlrd.open_workbook('D:/cookings.xlsx')
    sheet = wb.sheet_by_index(1)
    # For row 0 and column 0
    print(sheet.cell_value(0, 0))

    """for i in range(sheet.ncols):
        wh = sheet.cell_value(i+1,1)
        while(j<6):
            if(sheet.cell_value(i+1,j)!=''):
                dis.append(sheet.cell_value(i+1,j))
            j+=1

        while(t<14):
            if(sheet.cell_value(i+1,j)!=''):
                comp.append(sheet.cell_value(i+1,t))
            t+=1
        @Rule(weather(wh),NOT(diseases(dis)),components(comp))
        def ththththbt(self):
            print("******************ththbtata")"""

    # 1 almujdira_bel_bourgol
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          NOT(diseases('حساسية')),
          time_cooking(Tim >= (1)),
          components('برغل خشن'),
          components('بصل'),
          components('ملح'),
          components('عدس'),
          components('زيت'))
    def R_almujdira_bel_bourgol(self):
        print("You can cook : almujdira_bel_bourgol")

    # 1 almujdira_bel_risse
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (1)),
          components('رز'),
          components('بصل'),
          components('ملح'),
          components('عدس'),
          components('زيت'))
    def R_almujdira_bel_risse(self):
        print("You can cook : almujdira_bel_risse")

    # 2 alfarika
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (2)),
          NOT(OR(diseases('حساسية'),
                 diseases('قولون'), diseases('قلب'))),
          components('فريكة'),
          components('بصل'),
          components('ملح'),
          components('سمنة'),
          components('زيت'),
          components('لحم'),
          components('فلفل'))
    def R_alfarika(self):
        print("You can cook : alfarika")

    # 3 alkhabiza
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (0.25)),
          NOT(diseases('قلب')),
          components('خبيزة'),
          components('سمنة'),
          components('ثوم'),
          components('ملح'),
          components('كزبرة'),
          components('زيت'),
          components('لحم'),
          components('فلفل'))
    def R_alkhabiza(self):
        print("You can cook : alkhabiza")

    # 4 bamiatan_wa_bindura
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('بامية'),
          components('بندورة'),
          components('كزبرة'),
          components('ملح'),
          components('ثوم'),
          components('زيت'))
    def R_bamiatan_wa_bindura(self):
        print("You can cook : bamiatan_wa_bindura")

    # 5 bitataa_ealaa_hamid
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (1)),
          components('بطاطا'),
          components('بصل'),
          components('لحم'),
          components('ملح'),
          components('دبس بندورة'),
          components('زيت'),
          OR(components('رز'), components('برغل خشن')),
          components('شعيرية'))
    def R_bitataa_ealaa_hamid(self):
        print("You can cook : bitataa_ealaa_hamid")

    # 6 btataan_ealaa_hulu
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          components('بطاطا'),
          components('بصل'),
          components('حمص'),
          components('لحم'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_btataan_ealaa_hulu(self):
        print("You can cook : btataan_ealaa_hulu")

    # 7 ruzun_mae_biazlia
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('رز'),
          components('بازلياء'),
          components('ملح'),
          components('زيت'),
          OR(components('لحم')))
    def R_ruzun_mae_biazlia(self):
        print("You can cook : ruzun_mae_biazlia")

    # 8 ruza_mae_fawal
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('رز'),
          components('فول'),
          components('زيت'),
          components('ملح'),
          OR(components('لحم')))
    def R_ruza_mae_fawal(self):
        print("You can cook : ruza_mae_fawal")

    # 8 brgol_mae_fawal
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('برغل خشن'),
          components('فول'),
          components('زيت'),
          components('ملح'),
          OR(components('لحم')))
    def R_brgol_mae_fawal(self):
        print("You can cook : brgol_mae_fawal")

    # 9 shakiria
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          NOT(diseases('سكري')),
          NOT(diseases('قلب')),
          components('لبن'),
          components('لحم'),
          components('نشاء'),
          components('بصل'),
          components('رز'),
          components('شعيرية'),
          components('ملح'),
          components('زيت'))
    def R_shakiria(self):
        print("You can cook : shakiria")

    # 10 shwrbat_aleads
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (1)),
          NOT(diseases('فشل كلوي')),
          components('بصل'),
          components('عدس أحمر'),
          components('ملح'),
          components('زيت'),
          components('بهارات'))
    def R_shwrbat_aleads(self):
        print("You can cook : shwrbat_aleads")

    # 11 faswlya_biziat
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          NOT(diseases('سرطان')),
          components('فاصولياء'),
          components('بندورة'),
          components('لحم'),
          components('كزبرة'),
          components('ملح'),
          components('زيت'),
          components('ثوم'))
    def R_faswlya_biziat(self):
        print("You can cook : faswlya_biziat")

    # 12 faswlya_mae_rizin
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          components('فاصولياء'),
          components('بندروة'),
          components('لحم'),
          components('ملح'),
          components('بهارات'),
          components('كزبرة'),
          components('ثوم'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_faswlya_mae_rizin(self):
        print("You can cook : faswlya_mae_rizin")

    # 13 maraqat_faswlya_hubi
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قولون')),
          components('فاصولياء حب'),
          components('بندورة'),
          components('دبس بندورة'),
          components('لحم'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_maraqat_faswlya_hubi(self):
        print("You can cook : maraqat_faswlya_hubi")

    # 14 fawal_akhdur_ealaa_bid
    @Rule(OR(weather('لا يهم'), weather('حار')),
          time_cooking(Tim >= (0.5)),
          NOT(diseases('حساسية')),
          components('فول أخضر'),
          components('بيض'),
          components('ملح'),
          components('زيت'))
    def R_fawal_akhdur_ealaa_bid(self):
        print("You can cook : fawal_akhdur_ealaa_bid")

    # 15 fawalu_maqlaa
    @Rule(OR(weather('لا يهم'), weather('حار')),
          time_cooking(Tim >= (0.5)),
          NOT(diseases('سرطان')),
          NOT(diseases('قلب')),
          components('فول أخضر'),
          components('ثوم'),
          components('كزبرة'),
          components('ملح'),
          components('زيت'),
          components('سلق'))
    def R_fawalu_maqlaa(self):
        print("You can cook : fawalu_maqlaa")

    # 16 kari
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          NOT(diseases('بواسير')),
          components('بصل'),
          components('فليفلة خضراء'),
          components('لحم'),
          components('دبس بندورة'),
          components('رز كبسة'),
          components('ملح'),
          components('زيت'),
          components('فلفل'))
    def R_kari(self):
        print("You can cook : kari")

    # 17 kabab_hindiin
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          NOT(diseases('قلب')),
          components('بصل'),
          components('بندورة'),
          components('لحم مفروم'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_kabab_hindiin(self):
        print("You can cook : kabab_hindiin")

    # 18 kabisa
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          components('رز كبسة'),
          components('لحم'),
          components('بهارات كبسة'),
          components('ملح'),
          components('زيت'))
    def R_kabisa(self):
        print("You can cook : kabisa")

    # 19 kobaa
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (2.5)),
          NOT(diseases('حساسية')),
          NOT(diseases('قلب')),
          components('برغل'),
          components('لحم مفروم'),
          components('بصل'),
          components('ملح'),
          components('زيت'),
          components('بهارات'))
    def R_kobaa(self):
        print("You can cook : kobaa")

    # 20 kwaj_biadhnajan_ealaa_bindura
    @Rule(OR(weather('لا يهم'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('باذنجان'),
          components('بندورة'),
          components('ثوم'),
          components('ملح'),
          components('زيت'),
          components('نعنع'))
    def R_kwaj_biadhnajan_ealaa_bindura(self):
        print("You can cook : kwaj_biadhnajan_ealaa_bindura")

    # 21 kwaj_bitataan_ealaa_bindura
    @Rule(OR(weather('لا يهم'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('بطاطا'),
          components('بندورة'),
          components('بصل'),
          components('ملح'),
          components('زيت'),
          components('بهارات'))
    def R_kwaj_bitataan_ealaa_bindura(self):
        print("You can cook : kwaj_bitataan_ealaa_bindura")

    # 22 kwaj_bindurat_ealaa_bsl
    @Rule(OR(weather('لا يهم'), weather('حار')),
          time_cooking(Tim >= (0.5)),
          components('بندورة'),
          components('بصل'),
          components('ملح'),
          components('زيت'),
          components('لحم'),
          components('بهارات'))
    def R_kwaj_bindurat_ealaa_bsl(self):
        print("You can cook : kwaj_bindurat_ealaa_bsl")

    # 23 kwaj_kusaan_ealaa_bindura
    @Rule(OR(weather('لا يهم'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('كوسا'),
          components('بندورة'),
          components('ثوم'),
          components('ملح'),
          components('زيت'),
          components('نعنع'))
    def R_kwaj_kusaan_ealaa_bindura(self):
        print("You can cook : kwaj_kusaan_ealaa_bindura")

    # 24 kusana_bilaban
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قلب')),
          components('كوسا'),
          components('لحم مفروم'),
          components('بصل'),
          components('لبن'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_kusana_bilaban(self):
        print("You can cook : kusana_bilaban")

    # 25 maraqat_bamiatan
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          components('بامية'),
          components('بندورة'),
          components('لحم'),
          components('ثوم'),
          components('كزبرة'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_maraqat_bamiatan(self):
        print("You can cook : maraqat_bamiatan")

    # 26 maraqat_hams_ealaa_bindura
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('فشل كلوي')),
          components('بصل'),
          components('بندورة'),
          components('حمص'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_maraqat_hams_ealaa_bindura(self):
        print("You can cook : maraqat_hams_ealaa_bindura")

    # 27 maekirunat_ealaa_laban
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (0.5)),
          components('معكرونة'),
          components('لبن'),
          components('طحينة'),
          components('ثوم'),
          components('زيت زيتون'),
          components('ملح'))
    def R_maekirunat_ealaa_laban(self):
        print("You can cook : maekirunat_ealaa_laban")

    # 28 mafrakat_bitatana
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          NOT(diseases('حساسية')),
          components('بطاطا'),
          components('بيض'),
          components('ملح'),
          components('زيت'))
    def R_mafrakat_bitatana(self):
        print("You can cook : mafrakat_bitatana")

    # 29 mafrakat_kusanaan
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          NOT(diseases('حساسية')),
          components('كوسا'),
          components('بيض'),
          components('ملح'),
          components('زيت'))
    def R_mafrakat_kusanaan(self):
        print("You can cook : mafrakat_kusanaan")

    # 30 mafrakat_maekrunat_ealaa_bid
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (0.5)),
          NOT(diseases('حساسية')),
          components('معكرونة'),
          components('بيض'),
          components('ثوم'),
          components('ملح'),
          components('زيت'))
    def R_mafrakat_maekrunat_ealaa_bid(self):
        print("You can cook : mafrakat_maekrunat_ealaa_bid")

    # 31 mnnzlt_bydhanjan
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قلب')),
          components('باذنجان'),
          components('بصل'),
          components('لحم'),
          components('بندرورة'),
          components('ملح'),
          components('زيت'),
          components('رز'),
          components('شعيرية'))
    def R_mnnzlt_bydhanjan(self):
        print("You can cook : mnnzlt_bydhanjan")

    # 32 mandi
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('رز كبسة'),
          components('لحم'),
          components('ملح'),
          components('زيت'),
          components('بهارات مندي'))
    def R_mandi(self):
        print("You can cook : mandi")

    # 34 mansif
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (4)),
          NOT(diseases('حساسية')),
          NOT(diseases('قلب')),
          NOT(diseases('سكري')),
          components('برغل خشن'),
          components('رز'),
          components('لحم'),
          components('لبن'),
          components('جميد سائل'),
          components('نشاء'),
          components('سمنة'),
          components('ملح'),
          components('زيت'))
    def R_(self):
        print("يمكنك طبخ منسف مليحي")

    # 35
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          NOT(diseases('قلب')),
          components('بامية'),
          components('بندورة'),
          components('ثوم'),
          components('زيت'),
          components('ملح'),
          components('خبز'),
          components('لحم'))
    def R_(self):
        print("يمكنك طبخ بامية ديرية")

    # 36
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قولون')),
          components('ملوخية'),
          components('ثوم'),
          components('لحم'),
          components('زيت'),
          components('ملح'))
    def R_(self):
        print("يمكنك طبخ ملوخية")

    # 37
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قلب')),
          NOT(diseases('سكري')),
          components('كوسا'),
          OR(components('باذنجان'),
             components('بطاطا'),
             components('فليفلة خضراء')),
          components('زيت'),
          components('بندورة'),
          components('لحم'),
          components('حمض الليمون'),
          components('ملح'),
          components('نعنع'),
          components('رز'))
    def R_(self):
        print("يمكنك طبخ محاشي")

    # 38
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (4)),
          NOT(diseases('قلب')),
          components('قشة'),
          components('رز'),
          components('لحم مفروم'),
          components('مكسرات'),
          components('ثوم'),
          components('نعنع'),
          components('عصفر'),
          components('زيت'),
          components('ملح'))
    def R_(self):
        print("يمكنك طبخ قشة")

    # 39
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (2)),
          components('طحين'),
          components('لبن'),
          components('لحم مفروم'),
          #           OR(components('مكسرات'),components(W())),
          components('زيت'),
          components('ملح'),
          components('نشاء'))
    def R_(self):
        print("يمكنك طبخ ششبرك باللبن")

    # 40
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (2)),
          components('طحين'),
          components('دبس بندورة'),
          components('لحم مفروم'),
          #           OR(components('مكسرات'),components(W())),
          components('زيت'),
          components('ملح'),
          components('نشاء'))
    def R_(self):
        print("يمكنك طبخ ششبرك بدبس البندورة")

    # 41
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قولون')),
          NOT(diseases('قلب')),
          components('سمك'),
          components('بهارات سمك'),
          components('ملح'),
          components('زيت'),
          components('ليمون'))
    def R_(self):
        print("يمكنك طبخ سمك مقلي")

    # 42
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          NOT(diseases('قلب')),
          components('طحين'),
          components('لحم مفروم'),
          components('مكسرات'),
          components('زيت'),
          components('ملح'))
    def R_(self):
        print("يمكنك طبخ سم بوسك")

    # 43
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          NOT(diseases('قولون')),
          NOT(diseases('قلب')),
          components('بطاطا'),
          components('باذنجان'),
          components('زيت'),
          components('ملح'))
    def R_(self):
        print("يمكنك طبخ مقالي")

    # 44
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('بطاطا'),
          components('بندورة'),
          components('فليفلة'),
          components('ملح'),
          components('زيت'))
    def R_(self):
        print("يمكنك طبخ بطاطا بالصينية")

    # 45
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          components('رز كبسة'),
          components('باذنجان'),
          components('بندورة'),
          components('فليفلة خضراء'),
          components('ثوم'),
          components('لحم'))
    def R_(self):
        print("يمكنك طبخ مقلوبة")

    # 46
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          components('ورق عنب'),
          components('زيت'),
          components('بندورة'),
          components('لحم'),
          components('بهارات'),
          components('ملح'),
          components('زيت'),
          components('نعنع'),
          components('رز'))
    def R_(self):
        print("يمكنك طبخ يبرق بورق عنب")

    # 47
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          components('ملفوف'),
          components('زيت'),
          components('بندورة'),
          components('لحم'),
          components('بهارات'),
          components('ملح'),
          components('زيت'),
          components('نعنع'),
          components('رز'))
    def R_(self):
        print("يمكنك طبخ يبرق بالملفوف")

    # 48
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (2)),
          components('دجاج'),
          components('رز كبسة'),
          components('بازلاء'),
          components('جزر'),
          components('بطاطا'),
          components('مكسرات'),
          components('ملح'),
          components('زيت'))
    def R_(self):
        print("يمكنك طبخ الأوزي")

    # 49
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1.5)),
          components('دجاج'),
          components('كمون'),
          components('بصل'),
          components('بندورة'),
          components('ملح'),
          components('بهارات'), )
    def R_(self):
        print("يمكنك طبخ الشاورما العربي بالدجاج")

    # 50
    @Rule(OR(weather('لا يهم'), weather('بارد'), weather('حار')),
          time_cooking(Tim >= (1)),
          components('معلاق'),
          components('بصل'),
          components('ملح'),
          components('زيت'))
    def R_(self):
        print("يمكنك طبخ معلاق")

    # 51
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (0.5)),
          components('كشك'),
          components('لحم'),
          components('بصل'),
          components('زيت'),
          components('ملح'))
    def R_(self):
        print("يمكنك طبخ كشك تختاخ")

    # 52
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (0.5)),
          components('كشك'),
          components('لحم'),
          components('بصل'),
          components('بطاطا'),
          components('زيت'),
          components('ملح'),
          components('خبز'),
          components('ثوم'),
          components('نعنع'))
    def R_(self):
        print("يمكنك طبخ كشكية")

    # 53
    @Rule(OR(weather('لا يهم'), weather('بارد')),
          time_cooking(Tim >= (0.5)),
          components('شعيرية'),
          components('لحم'),
          components('ماجي'),
          components('دبس بندورة'))
    def R_(self):
        print("يمكنك طبخ شوربة ماجي")
    # 54


root = tk.Tk()
root.title("Foodie")
ico = PIL.Image.open('FOODIE1.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.configure(bg='white')
w = tk.Label(root, text='What Components are Available?', font=("Courier", 8, 'bold'), bg='white')
w.pack(side="left")
text = tk.Text(root, width=10, height=10, wrap=NONE)
vsb = tk.Scrollbar(root, command=text.yview)

text.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
text.pack(side="left", fill="y", expand=True)
COMPONENTS = ['باذنجان', 'فول', 'فاصولياء حب', 'سلق', 'حمص', 'كزبرة', 'بيض',
              'فريكة', 'ثوم', 'سمنة', 'فول أخضر', 'فاصولياء',
              'فليفلة خضراء', 'برغل', 'خبيزة', 'بهارات كبسة',
              'رز كبسة', 'عدس', 'جميد سائل', 'لحم', 'لبن',
              'لحم مفروم', 'نعنع', 'دبس بندورة', 'شعيرية', 'زيت',
              'بامية', 'زيت زيتون', 'بصل', 'بازلياء',
              'فلفل', 'بطاطا', 'عدس أحمر', 'رز', 'برغل خشن',
              'ملح', 'بهارات مندي', 'معكرونة', 'بهارات'
    , 'نشاء', 'طحينة', 'بندورة', 'كوسا', 'خبز',
              'ملوخية', 'دجاج', 'قشة', 'حمض الليمون',
              'مكسرات', 'عصفر', 'طحين', 'سمك',
              'ليمون', 'جزر', 'معلاق', 'كشك',
              'ماجي', 'قرع']
L_components = []
vars = []

for CM in COMPONENTS:
    var = StringVar()
    chk = Checkbutton(root, text=CM, variable=var, bg='white')
    text.window_create("end", window=chk)
    text.insert("end", "\n")
    vars.append(var)
text.configure(autoseparators=TRUE,state="disabled", borderwidth=0)


def state():
    return map((lambda var: var.get()), vars)


Diseases = ['سكري', 'قلب', 'قولون', 'بواسير', 'فشل كلوي', 'حساسية', 'سرطان']

w = tk.Label(root, text='What Diseases Do You Have?', font=("Courier", 8, 'bold'), bg='white')
w.pack(side="left")

text1 = tk.Text(root, width=15, height=15, wrap=WORD)

text1.pack(side="left", fill="none", expand=True)
vsb1 = tk.Scrollbar(root, command=text1.yview)
vsb1.pack(side="right", fill="none")
text1.configure(yscrollcommand=vsb1.set, borderwidth=0)
vars1 = []
L_diseases = []
for Dis in Diseases:
    var1 = StringVar()
    chk1 = Checkbutton(root, text=Dis, variable=var1, bg='white', border=0)
    text1.window_create("end", window=chk1)
    text1.insert("end", "\n")
    vars1.append(var1)
text1.configure(state="disabled")


def state_D():
    return map((lambda var1: var1.get()), vars1)


v = StringVar(root)
# Dictionary to create multiple buttons
values = {"بارد": "بارد",
          "حار": "حار",
          "لا يهم": "لا يهم"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
w = tk.Label(root, text='What\'s The Weather ?', font=("Courier", 8, 'bold'), bg='white')
w.pack(side="top")
for (text, value) in values.items():
    Radiobutton(root, text=text, variable=v, value=value, indicator=0, bg='white', borderwidth=0).pack(fill=X, ipady=5)

v_t = IntVar(root)
v_time = {"ربع ساعة": 0.25,
          "نصف ساعة": 0.5,
          "ساعة": 1,
          "ساعة ونصف": 1.5,
          "ساعتين": 2,
          "ساعتين ونصف": 2.5,
          "أربع ساعات": 4}
w = tk.Label(root, text='How Much Time Do You Have?', font=("Courier", 8, 'bold'), bg='white')
w.pack(side="top")
for (text, value) in v_time.items():
    Radiobutton(root, text=text, variable=v_t, value=value, indicator=0, bg='white', borderwidth=0).pack(fill=X,
                                                                                                         ipady=5)


def ok():
    print("The time available :")
    print(v_t.get())
    print("The Weather :")
    print(v.get())
    print("The Components :")
    for i in range(len(list(state()))):
        if list(state())[i] == '1':
            print(COMPONENTS[i])
            L_components.append(COMPONENTS[i])
    print("The Diseases :")
    for i in range(len(list(state_D()))):
        if list(state_D())[i] == '1':
            print(Diseases[i])
            L_diseases.append(Diseases[i])
    f_run()


def f_run():
    engine = FOODIE()
    engine.reset()
    engine.declare(time_cooking(Tim >= (v_t.get())))
    engine.declare(weather(v.get()))
    for cm in L_components:
        engine.declare(components(cm))
    for Di in L_diseases:
        engine.declare(diseases(Di))
    engine.run()


button = RoundedButton(root, text="Done", border_radius=4, padding=6, command=ok, color="#cda989")
button.pack(side="bottom")
root.mainloop()
