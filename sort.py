def quick_sort(lista_recnika):
    length = len(lista_recnika)
    if length <= 1:
        return lista_recnika
    else: 
        pivot = lista_recnika.pop(round(length/2)-1)
        pivot_key_list = pivot.keys()
        pivot_key = ""
        for key in pivot_key_list:
            pivot_key = key

    items_lower = []
    items_greater = []

    for recnik in lista_recnika:
        kljucevi = recnik.keys() #mora ovako iako ima samo 1 kljuc
        for kljuc in kljucevi:
            niz1 = recnik[kljuc]
            sum1 = niz1[0] + niz1[1]

            niz_pivot = pivot[pivot_key]
            sum2 = niz_pivot[0] + niz_pivot[1]

            if sum1 > sum2:
                items_greater.append(recnik)
            else:
                items_lower.append(recnik)
    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower)