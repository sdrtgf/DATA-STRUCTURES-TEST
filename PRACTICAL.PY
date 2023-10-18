catholic_martyrs = ["Achileo Kiwanuka, Adolphus ,LudigoMukasa, Ambrosius, Kibuuka, Anatoli, Kiriggwajjo, Andrew Kaggwa, Antanansio, Bazzekuketta, Bruno, Sserunkuuma, Charles Lwanga, Denis, Ssebuggwawo, Wasswa, Gonzaga Gonza, Gyavira Musoke, James, Buuzaabalyaawo, John Maria, Muzeeyi, Joseph Mukasa,Kizito,Lukka,Baanabakintu,Matiya Mulumba,Mbaga Tuzinde,MugaggaLubowa,Mukasa,Kiriwawanvu,Nowa Mawaggali,Ponsiano,Ngondwe"]





anglican_martyrs = ["Aaron Lubega,Apollo Kivebulaya,Eria Sebukyala,Fredrick Kizza,George Kizza,James Hannington,Janani Luwum,Joseph,Balikuddembe,Kizito,Mark Kakumba,Matia Mulumba,Nuhu Mbegu,Robert,Munyagayirwa,Samwiri Mukasa,Yefusa Namayanja,Yohana Mukasa,Yosefu Lugalama,Yowana Kitaka,Yowana Maria,Mukasa,Yowana Mukiibi,Yusufu Lugalama,Zakayo Lubega,"]



# question 3: 
# Write a function to determine the group of a martyr
def martyr_count(name):
    if name in anglican_martyrs and name in catholic_martyrs:
        return "Both"
    elif name in anglican_martyrs:
        return "Anglican"
    elif name in catholic_martyrs:
        return "Catholic"
    else:
        return "Not Found"

# Question 4: 
# Determine the group of the martyr named "Kizito"
kizito_group = martyr_count("Kizito")
print("Group of Kizito:", kizito_group)

# Question 5:
# Write a function to check if a name is present in both lists
def is_uganda_martyr(name):
    return name in anglican_martyrs and name in catholic_martyrs

# Check if a name matches Uganda Martyrs in both lists
name_to_check = "Kizito"
if is_uganda_martyr(name_to_check):
    print(f"{name_to_check} is a Uganda Martyr.")
else:
    print(f"{name_to_check} is not a Uganda Martyr.")