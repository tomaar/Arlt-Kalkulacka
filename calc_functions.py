import math

global FormatLog
global FormatAngle


# QOL
def qol(qol_list1):
    qol_const(qol_list1)
    qol_misc(qol_list1)
    qol_log(qol_list1)


def qol_misc(misc_list1):
    misc_count = 0
    for misc_var in misc_list1[:]:
        if misc_var == "prv" or misc_var == "p" \
                or misc_var == "P" or misc_var == "PRV" \
                or misc_var == "PRIME" or misc_var == "prvocislo":
            misc_list1[misc_count] = "prime"
        if misc_var == "prvo" or misc_var == "PRIMEQ":
            misc_list1[misc_count] = "primeq"
        misc_count += 1


def qol_const(const_list1):
    const_count = 0
    for const_var in const_list1:
        if const_var == "pi" or const_var == "Pi" \
                or const_var == "PI" or const_var == "pí" \
                or const_var == "Pí" or const_var == "PÍ" \
                or const_var == "π" or const_var == "ϖ" \
                or const_var == "Π":
            const_list1[const_count] = math.pi
        elif const_var == "e" or const_var == "E":
            const_list1[const_count] = math.e
        elif const_var == "φ" or const_var == "ϕ" or \
                const_var == "φῖ" or const_var == "Φ" \
                or const_var == "fi" or const_var == "fí" \
                or const_var == "Fí" or const_var == "FÍ" \
                or const_var == "phi" or const_var == "Phi" \
                or const_var == "PHI":
            const_list1[const_count] = (1+(5**(1/2)))/2
        const_count += 1


def qol_log(log_list1):
    log_count = 0
    for log_var in log_list1[:]:
        if log_var == "LOG" or log_var == "Log" \
                or log_var == "L" or log_var == "l" or \
                log_var == "lg" or log_var == "logarithmus" or \
                log_var == "logaritmus":
            log_list1[log_count] = "log"
        elif log_var == "logd" or log_var == "ld" or \
                log_var == "lgd":
            log_list1[log_count] = "log"
            log_list1.insert(log_count+1, 10)
        elif log_var == "ln" or log_var == "logn" \
                or log_var == "lon" or log_var == "loge" \
                or log_var == "le" or log_var == "logE" \
                or log_var == "lE":
            log_list1[log_count] = "log"
            log_list1.insert(log_count+1, math.e)
        elif log_var == "lb" or log_var == "logb":
            log_list1[log_count] = "log"
            log_list1.insert(log_count+1, 2)
        log_count += 1


# log s jedním číslem
def log_nn(nn_list1, nn_var1):
    global FormatLog
    if len(nn_list1) < nn_var1 + 3 \
            or type(nn_list1[nn_var1+2]) != float:
        if FormatLog == 1:
            nn_list1.insert(nn_var1+1, 10)
        elif FormatLog == 2:
            nn_list1.insert(nn_var1+1, math.e)
        elif FormatLog == 3:
            nn_list1.insert(nn_var1 + 1, 2)


# +, -
def sign(sign_list1):
    sign_count = 0
    for sign_var in sign_list1[:]:
        if sign_var == "-" or sign_var == "+":
            if (type(sign_list1[sign_count-1])) == float \
                    and sign_count > 0:
                sign_count += 1
            else:
                if sign_var == "-":
                    sign_list1[sign_count+1] = 0 - sign_list1[sign_count+1]
                del sign_list1[sign_count]
        else:
            sign_count += 1


# Str-float
def isnumber(isnumber_var):
    try:
        float(isnumber_var)
        return True
    except ValueError:
        return False


# Float-int
def intise(int_list1):
    if int_list1[0] == int(int_list1[0]):
        int_list1[0] = int(int_list1[0])


# Mezery
def space_del(space_del_list1):
    space_del_count = 0  # Počítadlo pořadí
    for space_del_var in space_del_list1[:]:
        if space_del_var == " ":
            del space_del_list1[space_del_count]
        else:
            space_del_count += 1


# Čárky
def comma(comma_list1):
    comma_count = 0
    for comma_var in comma_list1:
        if comma_var == ",":
            comma_list1[comma_count] = "."
        comma_count += 1


# Čárky
def numerise(num_list1):
    num_count = 0
    for num_var in num_list1:
        if isnumber(num_var):
            num_list1[num_count] = float(num_list1[num_count])
        num_count += 1


# Konkatenace
def conc(conc_list1):
    conc_type = 2  # Typ výrazu: 0 - číslo, 1 - písmeno, 2 - jiný znak
    conc_pos = -1  # Pozice výrazu
    for conc_var in conc_list1[:]:
        if conc_var.isnumeric() or conc_var == ".":
            if conc_type == 0:
                conc_list1[conc_pos] = \
                    conc_list1[conc_pos] + conc_list1[conc_pos+1]
                del conc_list1[conc_pos+1]
            else:
                conc_pos += 1
            conc_type = 0
        elif conc_var.isalpha():
            if conc_type == 1:
                conc_list1[conc_pos] = \
                    conc_list1[conc_pos] + conc_list1[conc_pos+1]
                del conc_list1[conc_pos + 1]
            else:
                conc_pos += 1
            conc_type = 1
        else:
            conc_pos += 1
            conc_type = 2


# Závorky
def brack_counter(brack_counter_list1):
    brack_counter_count = 0
    for brack_counter_var in brack_counter_list1:
        if brack_counter_var == "(":
            brack_counter_count += 1
    return brack_counter_count


def brack(brack_list1):
    brack_last = 0
    brack_list2 = []
    brack_repeat = brack_list1
    brack_counter(brack_repeat)
    for i in range(brack_counter(brack_repeat)):
        brack_pos = 0
        for brack_var in brack_list1:
            if brack_var == "(":
                brack_last = brack_pos
            brack_pos += 1
        while True:
            del brack_list1[brack_last]
            if brack_list1[brack_last] != ")":
                brack_list2.append(brack_list1[brack_last])
            else:
                calculate(brack_list2)
                brack_list1[brack_last] = brack_list2[0]
                brack_list2.clear()
                break


def angle_in(angle_list1, angle_var, angle_pos):
    global FormatAngle
    if angle_var == "sin" or angle_var == "cos" \
            or angle_var == "tan" or angle_var == "ctan" \
            or angle_var == "sec" or angle_var == "csec" \
            or angle_var == "sinh" or angle_var == "cosh" \
            or angle_var == "tanh" or angle_var == "ctanh" \
            or angle_var == "sech" or angle_var == "csech":
        if FormatAngle == 1:
            angle_list1[angle_pos + 1] \
                = (angle_list1[angle_pos + 1] / 180) * math.pi
        elif FormatAngle == 3:
            angle_list1[angle_pos + 1] \
                = angle_list1[angle_pos + 1] * math.pi
        elif FormatAngle == 4:
            angle_list1[angle_pos + 1] \
                = (angle_list1[angle_pos + 1] / 200) * math.pi


def angle_out(angle_list1, angle_var, angle_pos):
    global FormatAngle
    if angle_var == "asin" or angle_var == "acos" \
            or angle_var == "atan" or angle_var == "actan" \
            or angle_var == "asec" or angle_var == "acsec" \
            or angle_var == "asinh" or angle_var == "acosh" \
            or angle_var == "atanh" or angle_var == "actanh" \
            or angle_var == "asech" or angle_var == "acsech":
        if FormatAngle == 1:
            angle_list1[angle_pos] \
                = (angle_list1[angle_pos] / math.pi) * 180
        elif FormatAngle == 3:
            angle_list1[angle_pos] \
                = angle_list1[angle_pos] / math.pi
        elif FormatAngle == 4:
            angle_list1[angle_pos] \
                = (angle_list1[angle_pos] / math.pi) * 200


# Výpočet
def calculate(calc_list1):
    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "sin" or calc_var == "cos" \
                or calc_var == "tan" or calc_var == "ctan" \
                or calc_var == "sec" or calc_var == "csec" \
                or calc_var == "asin" or calc_var == "acos" \
                or calc_var == "atan" or calc_var == "actan" \
                or calc_var == "asec" or calc_var == "acsec" \
                or calc_var == "sinh" or calc_var == "cosh" \
                or calc_var == "tanh" or calc_var == "ctanh" \
                or calc_var == "sech" or calc_var == "csech" \
                or calc_var == "asinh" or calc_var == "acosh" \
                or calc_var == "atanh" or calc_var == "actanh" \
                or calc_var == "asech" or calc_var == "acsech":

            angle_in(calc_list1, calc_var, calc_pos)

            if calc_var == "sin":
                calc_list1[calc_pos] = sin(calc_list1[calc_pos + 1])
            elif calc_var == "cos":
                calc_list1[calc_pos] = cos(calc_list1[calc_pos + 1])
            elif calc_var == "tan":
                calc_list1[calc_pos] = tan(calc_list1[calc_pos + 1])
            elif calc_var == "ctan":
                calc_list1[calc_pos] = ctan(calc_list1[calc_pos + 1])
            elif calc_var == "sec":
                calc_list1[calc_pos] = sec(calc_list1[calc_pos + 1])
            elif calc_var == "csec":
                calc_list1[calc_pos] = csec(calc_list1[calc_pos + 1])
            elif calc_var == "asin":
                calc_list1[calc_pos] = asin(calc_list1[calc_pos + 1])
            elif calc_var == "acos":
                calc_list1[calc_pos] = acos(calc_list1[calc_pos + 1])
            elif calc_var == "atan":
                calc_list1[calc_pos] = atan(calc_list1[calc_pos + 1])
            elif calc_var == "actan":
                calc_list1[calc_pos] = actan(calc_list1[calc_pos + 1])
            elif calc_var == "asec":
                calc_list1[calc_pos] = asec(calc_list1[calc_pos + 1])
            elif calc_var == "acsec":
                calc_list1[calc_pos] = acsec(calc_list1[calc_pos + 1])
            elif calc_var == "sinh":
                calc_list1[calc_pos] = sinh(calc_list1[calc_pos + 1])
            elif calc_var == "cosh":
                calc_list1[calc_pos] = cosh(calc_list1[calc_pos + 1])
            elif calc_var == "tanh":
                calc_list1[calc_pos] = tanh(calc_list1[calc_pos + 1])
            elif calc_var == "ctanh":
                calc_list1[calc_pos] = ctanh(calc_list1[calc_pos + 1])
            elif calc_var == "sech":
                calc_list1[calc_pos] = sech(calc_list1[calc_pos + 1])
            elif calc_var == "csech":
                calc_list1[calc_pos] = csech(calc_list1[calc_pos + 1])
            elif calc_var == "asinh":
                calc_list1[calc_pos] = asinh(calc_list1[calc_pos + 1])
            elif calc_var == "acosh":
                calc_list1[calc_pos] = acosh(calc_list1[calc_pos + 1])
            elif calc_var == "atanh":
                calc_list1[calc_pos] = atanh(calc_list1[calc_pos + 1])
            elif calc_var == "actanh":
                calc_list1[calc_pos] = actanh(calc_list1[calc_pos + 1])
            elif calc_var == "asech":
                calc_list1[calc_pos] = asech(calc_list1[calc_pos + 1])
            elif calc_var == "acsech":
                calc_list1[calc_pos] = acsech(calc_list1[calc_pos + 1])
            del calc_list1[calc_pos + 1]

            angle_out(calc_list1, calc_var, calc_pos)

            calc_pos -= 1
            print(calc_list1)
    else:
        calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "prime":
            calc_list1[calc_pos] = prime(calc_list1[calc_pos + 1])
            del calc_list1[calc_pos + 1]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "primeq":
            calc_list1[calc_pos] = primeq(calc_list1[calc_pos + 1])
            del calc_list1[calc_pos + 1]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "log":
            log_nn(calc_list1, calc_pos)
            calc_list1[calc_pos] \
                = log(calc_list1[calc_pos + 2], calc_list1[calc_pos + 1])
            del calc_list1[calc_pos + 1]
            del calc_list1[calc_pos + 1]
            calc_pos -= 0
            print(calc_list1)
        else:
            calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "!":
            calc_list1[calc_pos] = fact(calc_list1[calc_pos - 1])
            del calc_list1[calc_pos - 1]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "nsd" or calc_var == "nsn":
            if calc_var == "nsd":
                calc_list1[calc_pos - 1] \
                    = nsd(calc_list1[calc_pos - 1], calc_list1[calc_pos + 1])
            else:
                calc_list1[calc_pos - 1] = \
                    nsn(calc_list1[calc_pos + 1], calc_list1[calc_pos - 1])
            del calc_list1[calc_pos]
            del calc_list1[calc_pos]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "^" or calc_var == "√":
            if calc_var == "^":
                calc_list1[calc_pos - 1] = \
                    power(calc_list1[calc_pos - 1], calc_list1[calc_pos + 1])
            else:
                calc_list1[calc_pos - 1] = \
                    root(calc_list1[calc_pos + 1], calc_list1[calc_pos - 1])
            del calc_list1[calc_pos]
            del calc_list1[calc_pos]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1

    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "*" or calc_var == "/":
            if calc_var == "*":
                calc_list1[calc_pos - 1] = \
                    mult(calc_list1[calc_pos - 1], calc_list1[calc_pos + 1])
            else:
                calc_list1[calc_pos - 1] = \
                    div(calc_list1[calc_pos - 1], calc_list1[calc_pos + 1])
            del calc_list1[calc_pos]
            del calc_list1[calc_pos]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1

    sign(calc_list1)
    calc_pos = 0
    for calc_var in calc_list1[:]:
        if calc_var == "+" or calc_var == "-":
            if calc_var == "+":
                calc_list1[calc_pos - 1] = \
                    add(calc_list1[calc_pos - 1], calc_list1[calc_pos + 1])
            else:
                calc_list1[calc_pos - 1] = \
                    sub(calc_list1[calc_pos - 1], calc_list1[calc_pos + 1])
            del calc_list1[calc_pos]
            del calc_list1[calc_pos]
            calc_pos -= 1
            print(calc_list1)
        else:
            calc_pos += 1


# Funkce
def add(var1, var2):  # Sčítání
    var0 = var1 + var2
    return var0


def sub(var1, var2):  # Odčítání
    var0 = var1 - var2
    return var0


def mult(var1, var2):  # Násobení
    var0 = var1 * var2
    return var0


def div(var1, var2):  # Dělení
    var0 = var1 / var2
    return var0


def power(var1, var2):  # Umocňování
    var0 = var1 ** var2
    return var0


def root(var1, var2):  # Odmocňování
    var0 = var1 ** (1 / var2)
    return var0


def log(var1, var2):  # Logaritmy
    var0 = math.log(var1, var2)
    return var0


def fact(var1):  # Faktoriály
    var0 = math.factorial(var1)
    return var0


def nsd(var1, var2):  # Největší společný dělitel
    var0 = math.gcd(int(var1), int(var2))
    return float(var0)


def nsn(var1, var2):  # Nejmenší společný násobek
    var0 = (var1*var2)/(math.gcd(int(var1), int(var2)))
    return float(var0)


def sin(var1):  # Sinus
    var0 = math.sin(var1)
    return var0


def cos(var1):  # Kosinus
    var0 = math.cos(var1)
    return var0


def tan(var1):  # Tangens
    var0 = math.tan(var1)
    return var0


def ctan(var1):  # Kotangens
    var0 = math.cos(var1)/math.sin(var1)
    return var0


def sec(var1):  # Sekans
    var0 = 1/math.cos(var1)
    return var0


def csec(var1):  # Kosekans
    var0 = 1/math.sin(var1)
    return var0


def asin(var1):  # Arkus sinus
    var0 = math.asin(var1)
    return var0


def acos(var1):  # Arkus kosinus
    var0 = math.acos(var1)
    return var0


def atan(var1):  # Arkus tangens
    var0 = math.atan(var1)
    return var0


def actan(var1):  # Arkus kotangens
    var0 = math.atan(1/var1)
    return var0


def asec(var1):  # Arkus sekans
    var0 = math.acos(1/var1)
    return var0


def acsec(var1):  # Arkus kosekans
    var0 = math.asin(1/var1)
    return var0


def sinh(var1):  # Hyperbolický sinus
    var0 = math.sinh(var1)
    return var0


def cosh(var1):  # Hyperbolický kosinus
    var0 = math.cosh(var1)
    return var0


def tanh(var1):  # Hyperbolický tangens
    var0 = math.tanh(var1)
    return var0


def ctanh(var1):  # Hyperbolický kotangens
    var0 = math.cosh(var1)/math.sinh(var1)
    return var0


def sech(var1):  # Hyperbolický sekans
    var0 = 1/math.cosh(var1)
    return var0


def csech(var1):  # Hyperbolický kosekans
    var0 = 1/math.sinh(var1)
    return var0


def asinh(var1):  # Hyperbolický arkus sinus
    var0 = math.asinh(var1)
    return var0


def acosh(var1):  # Hyperbolický arkus kosinus
    var0 = math.acosh(var1)
    return var0


def atanh(var1):  # Hyperbolický arkus tangens
    var0 = math.atanh(var1)
    return var0


def actanh(var1):  # Hyperbolický arkus kotangens
    var0 = math.atanh(1/var1)
    return var0


def asech(var1):  # Hyperbolický arkus sekans
    var0 = math.acosh(1/var1)
    return var0


def acsech(var1):  # Hyperbolický arkus kosekans
    var0 = math.asinh(1/var1)
    return var0


def prime(var1):
    var1 = int(var1)  # Zadaná proměnná
    prime_list1 = [2, 3, 5]  # Předdefinovaný seznam prvočísel
    prime_checked = prime_list1[-1]
    while len(prime_list1) < var1:  # Vnější cyklus while
        while True:  # Vnitřní cyklus while
            prime_check = 1
            prime_checked += 2
            for prime_var in prime_list1:
                if prime_var > math.sqrt(prime_checked):
                    break
                if prime_checked % prime_var == 0:
                    prime_check = 0
                    break
            if prime_check == 1:
                prime_list1.append(prime_checked)
                break
    var0 = prime_list1[var1-1]
    return var0


def primeq(var1):
    var1 = int(var1)  # Zadaná proměnná
    prime_list1 = [2, 3, 5]  # Předdefinovaný seznam prvočísel
    prime_checked = prime_list1[-1]
    while prime_checked < var1:  # Vnější cyklus while
        while True:  # Vnitřní cyklus while
            prime_check = 1
            prime_checked += 2
            for prime_var in prime_list1:
                if prime_var > math.sqrt(prime_checked):
                    break
                if prime_checked % prime_var == 0:
                    prime_check = 0
                    break
            if prime_check == 1:
                prime_list1.append(prime_checked)
                break
    if var1 == prime_checked or var1 == 2 or var1 == 3 or var1 == 5:
        return 1
    else:
        return 0


def calc_main(list1, settings_list1):
    global FormatLog
    global FormatAngle
    FormatLog = settings_list1[0]
    FormatAngle = settings_list1[1]

    space_del(list1)
    comma(list1)
    conc(list1)
    numerise(list1)
    qol(list1)
    brack(list1)
    calculate(list1)
    list1[0] = round(list1[0], 16 -
        int(math.floor(math.log10(abs(list1[0]))))-1)
    intise(list1)
