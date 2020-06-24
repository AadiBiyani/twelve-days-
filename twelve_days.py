christmas_day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
start_verse = ("On the ")
end_verse = ["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens", "four Calling Birds", "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]
seperator = ", "

def converttostr(end_verse, seperator):
   final_str = seperator.join(end_verse)
   return final_str

def recite(start_verse, end_verse):
    index = 0
    for i in range(12):
        mid_verse = (christmas_day[index] + " day of christmas my true love gave to me:")
        print (start_verse + mid_verse + converttostr(end_verse[0:index+1], seperator))
        index = index + 1
    pass
converttostr(end_verse, seperator)
recite(start_verse, end_verse)

