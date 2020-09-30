mytuple = ("J'ai", 1, 'ans')
print(mytuple)
print(type(mytuple))
mytuple = mytuple[:2] + (6, "ans")
print(mytuple)
(I, age, agepart2, old) = mytuple
print(I)
print(f"{age}{agepart2}")
def function(age):
    nextyear = age + 1
    tenyear = age + 10
    return (nextyear, tenyear)
a = function(5)
print(a)
HarryPotter = (("Daniel Radcliffe", "Rupert Grint", "Emma Watson"),
[("Philosopher's Stone", 2001),
 ("Chamber of Secrets", 2002),
 ("Prisoner of Azkaban", 2004),
 ("Goblet of Fire", 2005),
 ("Order of the Phoenix", 2007),
 ("Half Blood Prince", 2009),
 ("Deathly Hallows Part 1", 2010),
 ("Deathly Hallows Part 2", 2011) ])
print(HarryPotter)