day = "[Ss]en(in)?|[Ss]el(asa)?|[Rr]abu?|[Kk]am(is)?|[Jj]umat|[Ss]ab(tu)?|[Mm]inggu|kemarin|semalam|tadi|besok|lusa|kemaren"
var_day = "([Ss]en(in)?|[Ss]el(asa)?|[Rr]abu?|[Kk]am(is)?|[Jj]um(at)?|[Ss]ab(tu)?|[Mm]inggu)( lalu| (yang )?akan datang| mendatang| sebelumnya| setelahnya)"
var_day1 = "(([Ss]e |[Dd]ua |[Tt]iga |[Ee]mpat |[Ll]ima |[Ee]nam |[Tt]ujuh |[Dd]elapan |[Ss]embilan |[Ss]epuluh )?(hari|minggu)( sebelumnya| (yang )?lalu| mendatang| (yang )?akan datang| mendatang| sebelumnya| setelahnya))"
final_day = day + "|" + var_day + "|" + var_day1

month = "([Jj]an(uari)?|[FfPp]eb(r?uari)?|[Mm]ar(et)?|[Aa]pr(il)?|[Mm]ei|[Jj]u[nl]i?|[Aa]gustus|[Aa]ug|[Aa]gt|[Ss]ep(t(ember)?)?|[Oo](ck)t(ober)?|[Nn]o(vp)(ember)?|[Dd]es(ember)?)"
var_month = "(([Jj]an(uari)?|[FfPp]eb(r?uari)?|[Mm]ar(et)?|[Aa]pr(il)?|[Mm]ei|[Jj]u[nl]i?|[Aa]gustus|[Aa]ug|[Aa]gt|[Ss]ep(t(ember)?)?|[Oo](ck)t(ober)?|[Nn]o(vp)(ember)?|[Dd]es(ember)?)( lalu| (yang )?akan datang| mendatang| sebelumnya| setelahnya))"
var_month1 = "([Ss]e |[Dd]ua |[Tt]iga |[Ee]mpat |[Ll]ima |[Ee]nam |[Tt]ujuh |[Dd]elapan |[Ss]embilan |[Ss]epuluh )?bulan (depan|(yang )?lalu|lagi|(yang )?akan datang)|dari sekarang|mendatang|setelahnya|sebelumnya"
final_month = month + "|" + var_month + "|" + var_month1

date = "(([Tt]anggal)?( \d{2}| \d{1})|(\(?(\d{2}|\d{1}|\d{4})[-/](\d{2}|\d{1}|\d{4})[-/](\d{4}|\d{2}|\d{1})\)?))"
year = "(([Ss]e |[Dd]ua |[Tt]iga |[Ee]mpat |[Ll]ima |[Ee]nam |[Tt]ujuh |[Dd]elapan |[Ss]embilan |[Ss]epuluh )?tahun( sebelumnya| (yang )?lalu| mendatang| (yang )?akan datang| (yang )?mendatang| sebelumnya| setelahnya))"
year1 = "(([Tt]ahun)?( \d{4}| \d{2}))"
clock = "(([Pp]ukul )?\d{2}[:.]\d{2}( (WIB|wib|wita|WIT(A)?|wit(a)?|)?))"
misc = date + "|" + year + "|" + year1 + "|" + clock


def get_time():
    final = final_day + "|" + final_month + "|" + misc
    return final


def get_number():
    number = r" \d\d*((\.\d)?\d*)?|^\d\d*((\.\d)?\d*)?"
    return number
