def add_time(start, duration, dia_de_la_semana = False):
    
  dias_de_la_semana_index = {"monday" : 0, "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6}
  
  dias_de_la_semana_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duracion = duration.partition(":")
  horas_duracion = int(duracion[0])
  minutos_duracion = int(duracion[2])

  comienzo = start.partition(":")
  separacion_minutos = comienzo[2].partition(" ")
  horas_comienzo = int(comienzo[0])
  minutos_comienzo = int(separacion_minutos[0])
  am_pm = separacion_minutos[2]
  cambio_periodo = {"AM": "PM", "PM": "AM"}

  cantidad_dias = int(horas_duracion / 24)

  minuto_final = minutos_comienzo + minutos_duracion
  if minuto_final >= 60:
    horas_comienzo += 1
    minuto_final = minuto_final % 60
  cantidad_de_periodos = int((horas_comienzo + horas_duracion) / 12)
  hora_final = (horas_comienzo + horas_duracion) % 12 

  minuto_final = minuto_final if minuto_final > 9 else "0" + str(minuto_final)
  hora_final = hora_final = 12 if hora_final == 0 else hora_final
  if(am_pm == "PM" and horas_comienzo + (horas_duracion % 12) >= 12):
    cantidad_dias += 1

  am_pm = cambio_periodo[am_pm] if cantidad_de_periodos % 2 == 1 else am_pm
    
  tiempo_final = str(hora_final) + ":" + str(minuto_final) + " " + am_pm  
  if(dia_de_la_semana):
    dia_de_la_semana = dia_de_la_semana.lower()
    index = int((dias_de_la_semana_index[dia_de_la_semana]) + cantidad_dias) % 7
    nuevo_dia = dias_de_la_semana_array[index]
    tiempo_final += ", " + nuevo_dia

  if(cantidad_dias == 1):
    return tiempo_final + " " + "(next day)"
  elif(cantidad_dias > 1):
    return tiempo_final + " " + "(" + str(cantidad_dias) + " " + "days later" + ")"


  return tiempo_final