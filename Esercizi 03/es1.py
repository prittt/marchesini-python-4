import time

def timer(divisor=1_000_000, unit='ms'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter_ns()
            ret = func(*args, **kwargs)
            stop = time.perf_counter_ns()
            elapsed = (stop - start) / divisor
            print(f'Time elapsed: {elapsed}{unit}')
            return ret
        return wrapper
    return decorator


def farfallino1(s: str) -> str:
    ret = ''
    for c in s:
        ret += c
        if c in 'aeiou':
            ret += 'f' + c
    return ret


def farfallino2(s: str) -> str:
    return (s.replace('a', 'afa')
            .replace('e', 'efe')
            .replace('i', 'ifi')
            .replace('o', 'ofo')
            .replace('u', 'ufu'))


def farfallino3(s: str) -> str:
    vowels = "aeiou"
    return "".join(char + "f" + char if char in vowels else char for char in s)

import re
regex = re.compile(r'([aeiou])')
def farfallino4(s: str) -> str:
    return regex.sub(r'\1f\1', s)


@timer()
def test(func):
    assert func('ciao') == 'cifiafaofo'

    lorem = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce in condimentum leo. Cras mi elit, posuere a aliquam sed, ultricies sit amet ante. Duis nibh odio, efficitur nec auctor et, sagittis a odio. Nunc ac dictum sapien. Pellentesque ipsum tortor, porttitor nec mi sit amet, congue fringilla mi. Aenean ac magna id nisi fringilla fringilla tempus sit amet dui. Duis justo tortor, condimentum eget nisl quis, suscipit vehicula erat. Etiam vulputate varius massa, vitae dignissim odio laoreet at. Nullam orci tortor, ultrices ut urna ac, accumsan euismod nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus.
Nunc sollicitudin nunc in lacinia gravida. Vivamus vel libero sed tortor pretium luctus a sed mauris. Morbi non aliquet nibh, nec sodales urna. Vestibulum sit amet luctus lorem, ac pulvinar sapien. Mauris elit mauris, interdum non viverra in, congue sed lectus. Phasellus eget sagittis mauris. Donec nec tortor id ante mollis semper eu ut turpis. Integer a magna vitae risus suscipit porttitor ut quis dui. Vivamus aliquam dolor in tempor viverra. Aliquam aliquam laoreet sodales. Pellentesque pellentesque, orci vel congue pulvinar, sapien nulla sollicitudin leo, in tempor diam turpis non ex. Quisque tempor velit pulvinar est commodo euismod. Pellentesque nec auctor turpis, quis eleifend est. Aliquam elementum ligula non diam cursus blandit. Duis sed dui nec magna hendrerit suscipit.
Phasellus nec rutrum diam. Proin aliquet semper lacus, sit amet consequat tortor vehicula eget. Nulla metus purus, ultricies rhoncus odio et, tempus aliquet augue. Nullam accumsan aliquam erat non sollicitudin. Integer laoreet, neque ut accumsan condimentum, augue felis tincidunt nisi, at porttitor tortor eros non est. Fusce et auctor dolor, ut eleifend nunc. Pellentesque posuere suscipit purus non rutrum.
In eu suscipit neque. Sed mattis nisl at justo elementum, sed ultrices enim sagittis. Nunc cursus urna justo, nec congue ligula cursus quis. Mauris lobortis, urna in pharetra vulputate, massa velit congue elit, nec vestibulum velit eros at eros. Nulla vitae vehicula neque. Ut euismod maximus ante vitae efficitur. Suspendisse vestibulum quis massa sit amet pretium. Phasellus congue faucibus sem sed accumsan. Mauris lacinia purus in justo maximus aliquet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum convallis euismod ex varius maximus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
Pellentesque pellentesque auctor ligula a maximus. Integer sagittis nulla at orci dignissim vulputate. Integer fermentum feugiat arcu ac sollicitudin. Sed vel arcu non est tristique porta. Donec nulla ex, cursus sit amet tempus et, ornare et metus. Aliquam vestibulum est lectus, eu tincidunt mauris consequat vel. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam consequat sed justo ac vestibulum. Nam in nibh vel felis tempor mollis. Nam tellus mi, interdum id tincidunt at, scelerisque feugiat neque.'''

    assert func(lorem) == 'Loforefem ifipsufum dofolofor sifit afamefet, cofonsefectefetufur afadifipifiscifing efelifit. Fufuscefe ifin cofondifimefentufum lefeofo. Crafas mifi efelifit, pofosufueferefe afa afalifiqufuafam sefed, ufultrificifiefes sifit afamefet afantefe. Dufuifis nifibh ofodifiofo, efeffificifitufur nefec afaufuctofor efet, safagifittifis afa ofodifiofo. Nufunc afac difictufum safapifiefen. Pefellefentefesqufuefe ifipsufum tofortofor, poforttifitofor nefec mifi sifit afamefet, cofongufuefe frifingifillafa mifi. Aefenefeafan afac mafagnafa ifid nifisifi frifingifillafa frifingifillafa tefempufus sifit afamefet dufuifi. Dufuifis jufustofo tofortofor, cofondifimefentufum efegefet nifisl qufuifis, sufuscifipifit vefehificufulafa eferafat. Etifiafam vufulpufutafatefe vafarifiufus mafassafa, vifitafaefe difignifissifim ofodifiofo lafaoforefeefet afat. Nufullafam oforcifi tofortofor, ufultrificefes ufut ufurnafa afac, afaccufumsafan efeufuifismofod nufunc. Inteferdufum efet mafalefesufuafadafa fafamefes afac afantefe ifipsufum prifimifis ifin fafaufucifibufus.\nNufunc sofollificifitufudifin nufunc ifin lafacifinifiafa grafavifidafa. Vifivafamufus vefel lifibeferofo sefed tofortofor prefetifiufum lufuctufus afa sefed mafaufurifis. Moforbifi nofon afalifiqufuefet nifibh, nefec sofodafalefes ufurnafa. Vefestifibufulufum sifit afamefet lufuctufus loforefem, afac pufulvifinafar safapifiefen. Mafaufurifis efelifit mafaufurifis, ifinteferdufum nofon vifiveferrafa ifin, cofongufuefe sefed lefectufus. Phafasefellufus efegefet safagifittifis mafaufurifis. Dofonefec nefec tofortofor ifid afantefe mofollifis sefempefer efeufu ufut tufurpifis. Intefegefer afa mafagnafa vifitafaefe rifisufus sufuscifipifit poforttifitofor ufut qufuifis dufuifi. Vifivafamufus afalifiqufuafam dofolofor ifin tefempofor vifiveferrafa. Alifiqufuafam afalifiqufuafam lafaoforefeefet sofodafalefes. Pefellefentefesqufuefe pefellefentefesqufuefe, oforcifi vefel cofongufuefe pufulvifinafar, safapifiefen nufullafa sofollificifitufudifin lefeofo, ifin tefempofor difiafam tufurpifis nofon efex. Qufuifisqufuefe tefempofor vefelifit pufulvifinafar efest cofommofodofo efeufuifismofod. Pefellefentefesqufuefe nefec afaufuctofor tufurpifis, qufuifis efelefeififefend efest. Alifiqufuafam efelefemefentufum lifigufulafa nofon difiafam cufursufus blafandifit. Dufuifis sefed dufuifi nefec mafagnafa hefendreferifit sufuscifipifit.\nPhafasefellufus nefec rufutrufum difiafam. Profoifin afalifiqufuefet sefempefer lafacufus, sifit afamefet cofonsefequfuafat tofortofor vefehificufulafa efegefet. Nufullafa mefetufus pufurufus, ufultrificifiefes rhofoncufus ofodifiofo efet, tefempufus afalifiqufuefet afaufugufuefe. Nufullafam afaccufumsafan afalifiqufuafam eferafat nofon sofollificifitufudifin. Intefegefer lafaoforefeefet, nefequfuefe ufut afaccufumsafan cofondifimefentufum, afaufugufuefe fefelifis tifincifidufunt nifisifi, afat poforttifitofor tofortofor eferofos nofon efest. Fufuscefe efet afaufuctofor dofolofor, ufut efelefeififefend nufunc. Pefellefentefesqufuefe pofosufueferefe sufuscifipifit pufurufus nofon rufutrufum.\nIn efeufu sufuscifipifit nefequfuefe. Sefed mafattifis nifisl afat jufustofo efelefemefentufum, sefed ufultrificefes efenifim safagifittifis. Nufunc cufursufus ufurnafa jufustofo, nefec cofongufuefe lifigufulafa cufursufus qufuifis. Mafaufurifis lofobofortifis, ufurnafa ifin phafarefetrafa vufulpufutafatefe, mafassafa vefelifit cofongufuefe efelifit, nefec vefestifibufulufum vefelifit eferofos afat eferofos. Nufullafa vifitafaefe vefehificufulafa nefequfuefe. Ut efeufuifismofod mafaxifimufus afantefe vifitafaefe efeffificifitufur. Sufuspefendifissefe vefestifibufulufum qufuifis mafassafa sifit afamefet prefetifiufum. Phafasefellufus cofongufuefe fafaufucifibufus sefem sefed afaccufumsafan. Mafaufurifis lafacifinifiafa pufurufus ifin jufustofo mafaxifimufus afalifiqufuefet. Inteferdufum efet mafalefesufuafadafa fafamefes afac afantefe ifipsufum prifimifis ifin fafaufucifibufus. Vefestifibufulufum cofonvafallifis efeufuifismofod efex vafarifiufus mafaxifimufus. Vefestifibufulufum afantefe ifipsufum prifimifis ifin fafaufucifibufus oforcifi lufuctufus efet ufultrificefes pofosufueferefe cufubifilifiafa cufurafaefe;\nPefellefentefesqufuefe pefellefentefesqufuefe afaufuctofor lifigufulafa afa mafaxifimufus. Intefegefer safagifittifis nufullafa afat oforcifi difignifissifim vufulpufutafatefe. Intefegefer fefermefentufum fefeufugifiafat afarcufu afac sofollificifitufudifin. Sefed vefel afarcufu nofon efest trifistifiqufuefe pofortafa. Dofonefec nufullafa efex, cufursufus sifit afamefet tefempufus efet, ofornafarefe efet mefetufus. Alifiqufuafam vefestifibufulufum efest lefectufus, efeufu tifincifidufunt mafaufurifis cofonsefequfuafat vefel. Clafass afaptefent tafacifitifi sofocifiofosqufu afad lifitoforafa toforqufuefent pefer cofonufubifiafa nofostrafa, pefer ifincefeptofos hifimefenafaefeofos. Nafam cofonsefequfuafat sefed jufustofo afac vefestifibufulufum. Nafam ifin nifibh vefel fefelifis tefempofor mofollifis. Nafam tefellufus mifi, ifinteferdufum ifid tifincifidufunt afat, scefeleferifisqufuefe fefeufugifiafat nefequfuefe.'

def main():
    test(farfallino1)
    test(farfallino2)
    test(farfallino3)
    test(farfallino4)

if __name__ == "__main__":
    main()
    

