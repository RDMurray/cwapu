# Version 4
translations = {
	'en': {
		'welcome_message': "\nCWAPU - VERSION: {version} BY GABE - IZ4APU.\n\t----UTILITIES FOR YOUR CW----\n\t\tLaunch: {count}. Type 'm' for menu.",
		'chars_to_next_report_progress': "Current section completion:\n+{s} -> ({x} / {y}) = {z}% (-{w}) to next report generation.",
		'reports_disabled': "Automatic report generation is disabled.",
		'custom_set_use_prefill_prompt': "Start with a pre-filled character group?",
		'yes_key_default': "y",
		'custom_set_prefill_failed_no_chars': "Prefill failed: no valid characters available.",
		'custom_set_modify_prompt_intro': "Enter/toggle characters. Press Enter when done.",
		'invoking_custom_set_editor': "Starting Custom group editor...",
		'custom_set_updated_short_feedback': "Custom set: {num_chars} chars.", # For .y command feedback
		'menu_rx_switcher_parole': "Words",
		'menu_rx_switcher_lettere': "Letters",
		'menu_rx_switcher_numeri': "Numbers",
		'menu_rx_switcher_simboli': "Symbols",
		'menu_rx_switcher_qrz': "QRZ",
		'menu_rx_switcher_custom': "Custom",
		'switcher_status_on_label': "ENABLED",
		'switcher_status_off_label': "disabled",
		'rx_switcher_menu_title': "Rx Exercises - Select Types (Enter to start):",
		'rx_switcher_menu_prompt': "Choose (1-6) or Enter: ",
		'rx_switcher_no_selection_error': "No exercise mode selected! Please activate at least one switcher.",
		'rx_switcher_group_length_prompt': "Group length (1-7 for Letters/Numbers/Symbols/Custom):",
		'rx_switcher_invalid_length_error': "Invalid length. Please enter a number from 1 to 7.",
		'parole_filter_no_results_with_saved': "Saved word filter yielded no results. 'Words' switcher disabled.",
		'parole_filter_use_dot_command': "Word filter not set/valid. Use '.t #-#' in Settings (k). 'Words' switcher disabled.",
		'parole_filter_applied_from_settings': "Word filter applied from settings ({count} words).",
		'custom_set_invoking': "Starting custom group configuration...",
		'custom_set_not_created_deactivating': "Custom group not created or invalid. 'Custom' switcher disabled.",
		'custom_set_loaded_from_settings': "Custom group loaded from settings: [{set_string}]",
		'invalid_menu_choice': "Invalid choice.",
		'parole_filter_not_set_error': "Error: 'Words' active but filter is not set or yields no results. Use '.t #-#'.",
		'mixed_exercise_types_label': "Mixed ({types})",
		'error_no_item_generated_rx': "Error: Could not generate exercise item with current selections. Check Rx menu settings.",
		'no_key_default': "n",
		'custom_set_prefilled_with_errors': "Group pre-filled with frequent errors: {chars}",
		'custom_set_prefilled_with_random': "Group pre-filled with random characters: {chars}",
		'delta_rate_specific_label_short': "Δ% Specific Error Rate",
		'no_error_variations_to_display': "No significant character error variations to display.",
		'no_previous_data_for_variations': "Previous data not available to calculate variations.",
		'no_detailed_errors_to_display': "No detailed errors to display in the chart.",
		'no_errors_recorded_for_block': "No errors recorded for this block of sessions.",
		'visualization_to_be_implemented': "Visualization to be implemented", 
		'metric': "Metric",
		'current_value': "Current Value",
		'previous_value': "Previous Value",
		'error_count_header': "Error Count",
		'perc_vs_total_chars_header': "% of Total Chars",
		'perc_vs_spec_char_header': "% of Spec. Char Sent", # Leggermente più esplicito per un'intestazione
		'of_specific_char_sent_count': "of {count} '{char_upper}' sent", # Usato dentro una cella per dettaglio
		'variations_vs_block_of': "Variations vs. previous block of {count} exercises", # Sottotitolo per tabella variazioni
		'curr_error_count_header': "Curr. Err.", # Intestazione breve per tabella variazioni
		'curr_perc_vs_total_header': "Curr. %Tot", # Intestazione breve
		'curr_perc_vs_spec_header': "Curr. %Spec", # Intestazione breve
		'prev_error_count_header': "Prev. Err.", # Intestazione breve
		'prev_perc_vs_total_header': "Prev. %Tot", # Intestazione breve
		'prev_perc_vs_spec_header': "Prev. %Spec", # Intestazione breve
		'delta_rate_total_header': "Δ% Tot. Chars", # Intestazione breve per variazione % su tot. caratteri
		'delta_rate_spec_header': "Δ% Spec. Char", # Intestazione breve per variazione % su caratt. specifico
		'of_n_sent': "of {count} sent", # Etichetta generica per dettaglio in cella (conteggio inviati)
		'delta_rate_total_label': "Δ Rate (vs total chars):",
		'delta_rate_specific_label': "Δ Rate (vs '{char_upper}' sent):",
		'rate_change_specific_char':"Rate change (of '{char_upper}' sent)",
		'error_detail_line_format':"'{char_upper}': {count} ({perc_vs_total:.2f}% {of_total_chars_label}, {perc_vs_specific:.2f}% {of_specific_char_sent_label})",
		'of_specific_char_sent':"of '{char_upper}' sent",
		'error_saving_graphical_file: ':"Error saving graphical file {filename}: {error}",
		'error_generating_graphical_report: ':"Error generating graphical report: {error}",
		'graphical_report_saved_to':"Graphical report saved to: {filename}",
		'avg_wpm_of_session_avgs_label':"Avg WPM (average of sessions)",
		'report_header_appname': "CWAPU",
		'historical_stats_report_title': "Historical Rx Exercises Statistics Report",
		'report_generated_on': "Report generated on",
		'stats_based_on_exercises': "Statistics based on {count} exercises",
		'overall_speed_stats': "Overall Speed Statistics",
		'min_wpm': "Min WPM",
		'max_wpm': "Max WPM",
		'avg_wpm_cpm_based': "Avg WPM (CPM-based)",
		'overall_error_stats': "Overall Error Statistics",
		'total_chars_sent_in_block': "Total characters sent (in block)",
		'total_errors_in_block': "Total errors (in block)",
		'error_details_by_char': "Error details by character",
		'of_total_chars': "of total chars",
		'variations_from_previous_block': "Variations From Previous Block",
		'exercises_articles': "exercises", # Used like: {count} exercises
		'vs': "vs.",
		'change': "Change",
		'overall_error_rate': "Overall error rate",
		'error_details_variations': "Character Error Details Variations",
		'no_errors_in_either_block': "No errors recorded in either reference block.",
		'rate_change_char': "Rate change",
		'unexpected_error_generating_report':"Unexpected error generating report: {e}",
		'error_saving_historical_report':"Error saving historical report {filename}: {e}",
		'historical_report_saved_to':"Historical report saved to: {filename}",
		'no_sessions_in_current_block_for_report':"No sessions in current block to report.",
		'not_a_valid_language': "Not a valid language",
		'no_historical_data_to_report':"No historical data available to report.",
		'generating_historical_report':"Generating historical report...",
		'select_language': "Select your language / Seleziona la lingua: ",
		'menu_prompt': "It's not a command!",
		'fix_yes': "Do you want the cw stay at the same speed?	(y|n)> ",
		'exit_message': "\nI hope to see you soon - 73 de IZ4APU TU EE",
		'attention_message': "Attention! Please read carefully.\nFor the reception exercises, (r) from the main menu, CWAPU uses the file words.txt, which must be located in the folder from which you launched cwapu.py or cwapu.exe. If this file does not exist, create one with a text editor and write some words in it, one word per line, then save it.\nThe WordsCreator procedure allows you to scan all the txt files contained in the folders you indicate and add all the words from those files to words.txt. The words will be added uniquely, meaning they will all be different from each other.\nThe file produced by this process will be named words_updated.txt. Check it with a text editor and, if you are satisfied with it, rename it to words.txt, replacing the existing words.txt.\nYou can repeat this operation as many times as you like: words_updated.txt will contain the words from words.txt plus all those collected from the newly processed .txt files.",
		'filter_words_prompt': "\nLet's filter the words set to using with the exercise\nPlease type minimum.maximum length of the words you want to be chosen randomly. e.g. 3.6\nwill choose words with length in between 3 and 6 characters only.\nType enter to use the whole dictionary",
		'insert_min_max': "Minimum.Maximum: ",
		'not_numbers': "You haven't inserted numbers",
		'try_again': "Try again",
		'filtering_range': "Filtering words which are in {mn}/{mx} range of length.",
		'confirm_word_count': "{word_count} words, are you ok with it? (y|n)> ",
		'custom_set_prompt': "Type all characters you want to practice on. (minimum of 2) Empty line to proceed",
		'transmitting_exercise': "Transmitting exercise.\nHere you're going to have random pseudo-calls and numbers,\n\ttry to play them on your favourite CW key.\nAny key to go on, ESCAPE to close the App.",
		'press_any_key': "Press any key when you're ready to start.",
		'bye_message': "Bye for now, back to main menu.",
		'counting_prompt': "Counting, YES or NO?\nSpacebar means: group received;\nAny other key means: group lost;\nPress ESCAPE to go back to main menu.",
		'exercise_number': "Exercise number {esnum}:",
		'total_correct': "Total: {cont}, correct: {corr}, mistakes(%): {pde:.2f}%.",
		'passed': "Passed!",
		'failed': "Failed: {difference:.2f}% to the threshold.",
		'report_saved': "Report saved on CW_Diary.txt",
		'note_on_exercise': "\nNote on this exercise: ",
		'empty_note': "Note: empty",
		'groups_received_few': "Groups received {cont} up to 100: exercise not saved on disk.",
		'session_saved': "Session {session_number}, lasts: {duration} has been saved on disk.",
		'menu_main': {
			"c": "Counting results",
			"k": "Keyboard and CW settings",
			"l": "Listen to clipboard",
			"m": "Shows Menu",
			"q": "To quit this app",
			"r": "Receiving exercise",
			"t": "Transmitting exercise",
			"w": "Create your own word dictionary",
			"z": "Select your language"
		},
		'menu_rx': {
			"1": "Pseudo-calls",
			"2": "Groups"
		},
		'menu_rx_kind': {
			"1": "Letters only (A to Z)",
			"2": "Numbers only (0 to 9)",
			"3": "Letters and Numbers (A to Z and 0 to 9)",
			"4": "Custom set (let's decide which symbols you want to work on)",
			"5": "Words (words picked up from a customizable file)"
		},
		'select_exercise': "Now select which exercise do you want to take:",
		'please_just_1_or_2': "Please, just 1 or 2",
		'choose_a_number': "Choose a number please",
		'give_length': "Give me the length of the group between 1 and 7: ",
		'filter_words_set': "\nLet's filter the words set to use with the exercise\nPlease type minimum.maximum length of the words you want to be chosen randomly. e.g. 3.6\nwill choose words with length in between 3 and 6 characters only.\nType enter to use the whole dictionary",
		'careful_type': "Now, careful. Type the {kindstring} you hear.\nGiving an empty line (or adding a ?) will gift you a second listen to the {kindstring}.\n\tTo stop, just type a '.' (full stop) followed by enter.\nENJOY. \tPress any key when you're ready to start.",
		'begin_session': "Let's begin session {sessions}!",
		'over_check': "It's over! Now let me check what we've got.",
		'received_too_few': "You received too few {kindstring} to generate consistent statistics.",
		'time_to_receive': "\nTime to receive? Yep, you're at the right place. Let's go!\n\tLoading the status of your progress and check for dictionary database...",
		'dictionary_loaded': "Word's dictionary loaded with {word_count} words.",
		'file_not_found': "File words.txt not found. Please provide a dictionary file: 1 word per line.",
		'first_class': "Oops, this is your first class, probably. So I'm creating the record.",
		'got_data': "I got your data from disk, so:\nYour actual WPM is {wpm} and you did {sessions} sessions.\nI sent to you {totalcalls} total pseudo-calls or groups, and you got {totalget} of them, while {totalwrong} were missed\nYour overall time receiving pseudo-calls is {totaltime}.",
		'set_wpm': "Do you want to set your WPM? Enter to accept {wpm}> ",
		'h_keyboard':
			"Welcome to the section where you can listen to CW and configure all its parameters.\n" \
			"These parameters will be valid and active throughout CWAPU and will be saved automatically when you exit the app.\n" \
			"Now, please read the following carefully:\n" \
			"\tPress Enter without typing anything to exit and return to the main menu;\n" \
			"\ttype .w followed by a numeric value to set the WPM;\n" \
			"\ttype .h followed by a value for the pitch of the CW note peak you want to use;\n" \
			"\ttype .l followed by a value to set the dash length, default is 30;\n" \
			"\ttype .s followed by a value to set the space length, default is 50;\n" \
			"\ttype .p just like .s but for dots;\n" \
			"\ttype .v followed by a value between 0 and 100 to set the volume;\n" \
			"\ttype .f1 .f2 .f3 or .f4 to change the waveform;\n" \
			"\ttype .m followed by milliseconds to set the fade in and out for the CW note;\n" \
			"\ttype .g followed by a value to set the number of exercises for global statistics;\n" \
			"\ttype .x followed by a value to set how often (in characters) to update global stats;\n" \
			"\ttype .t #-# where # are the min-max values of words lenght to choose from dictionary;\n" \
			"\ttype .y to set a customized group of characters to train with;\n" \
			"\ttype .sr to set the sample rate to send to your sound card;\n" \
			"\ttype ? to see this help message;\n" \
			"\ttype ?? to display the set parameters;\n" \
			"\ttype .rs to reset CW to the standard 1/3 weight\n" \
			"\ttype .sv <text> to save the CW to a .wav file\n",
		'empty_clipboard': "empty",
		'not_a_command': "It's not a command!",
		'press_m_for_menu': "\nCWAPU - VERSION: {version} BY GABE - IZ4APU.\n\t----UTILITIES FOR YOUR CW----\n\t\tPress 'm' for menu.",
		'o_set_loaded':"General settings loaded",
		'o_set_created':"General settings to default",
		'o_set_saved':"General settings saved on disk.",
		'l_set':"Application language set to English",
		'counting_exercise_report': "Counting exercise #{esnum} performed on {date} at {time} minutes:\n",
		'total_correct_report': "Total: {cont}, correct: {corr}, mistakes(%): {pde:.2f}%.\n",
		'note_with_text': "Note: {nota}\n***\n",
		'no_mistakes_recorded': "No character mistakes recorded in this session.",
		'session_summary': "In this session #{sessions}, I sent {calls} {kindstring} to you and you got {callsget_len} of them: {percentage:.1f}%",
		'how_many': "\nHow many do you want to receive? (ENTER for endless)> ",
		'first_shot': "\t{first_shot} of these have been taken at the first shot: {first_shot_percentage:.1f}%",
		'with_repetition': "\twhile {repetitions} {kindstring} with repetition: {repetitions_percentage:.1f}%.",
		'speed_summary': "You ran with a minimum speed of {minwpm} up to {maxwpm}: range of {range_wpm} WPM.\n\tAverage receiving speed: {average_wpm:.1f} WPM.",
		'character_mistakes': "Character: mistakes = Percentage",
		'total_mistakes': "\nTotal mistakes: {global_mistakes} on {send_char} = {mistake_percentage:.2f}%",
		'receiving_exercise_report': "\nReceiving exercise #{sessions} performed on {date} at {time} minutes:\n",
		'never_misspelled': "\nNever misspelled characters: {good_letters}",
		'list_of_wrong_words': "\nList of wrong received words:",
		'wrong_word_entry': "\n\t({k}) TX: {tx}, RX: {rx}, DIF: {dif};"
		#Qen
	},
	'it': {
		'welcome_message': "\nCWAPU - VERSIONE: {version} DI GABRY - IZ4APU.\n\t----UTILITÀ PER IL TUO CW----\n\t\tLancio app: {count}. Scrivi 'm' per il menu.",
		'list_of_wrong_words': "\nElenco delle parole copiate male:",
		'wrong_word_entry': "\n\t({k}) TX: {tx}, RX: {rx}, DIF: {dif};",
		'select_language': "Seleziona la lingua: ",
		'menu_prompt': "Non è un comando valido!",
		'exit_message': "\nSpero di rivederti presto - 73 de IZ4APU TU EE",
		'receiving_exercise_report': "\nEsercizio di ricezione #{sessions} eseguito il {date} alle {time} minuti:\n",
		'attention_message': "Attenzione! Si prega di leggere attentamente.\nPer gli esercizi di ricezione, (r) dal menu principale, CWAPU utilizza il file words.txt, che deve essere situato nella cartella da cui hai lanciato cwapu.py o cwapu.exe. Se questo file non esiste, creane uno con un editor di testo e scrivi alcune parole al suo interno, una parola per linea, quindi salva.\nLa procedura WordsCreator ti permette di scansionare tutti i file txt contenuti nelle cartelle che indichi e aggiungere tutte le parole da questi file a words.txt. Le parole saranno aggiunte unicamente, cioè saranno tutte diverse tra loro.\nIl file prodotto da questo processo sarà denominato words_updated.txt. Controllalo con un editor di testo e, se sei soddisfatto, rinominalo in words.txt, sostituendo l'esistente words.txt.\nPuoi ripetere questa operazione tutte le volte che vuoi: words_updated.txt conterrà le parole da words.txt più tutte quelle raccolte dai nuovi file .txt elaborati.",
		'filter_words_prompt': "\nApplichiamo un filtro al dizionario delle parole\nPer favore, digita la lunghezza minima.massima delle parole che vuoi vengano usate nell'esercizio. Es. 3.6\nsceglierà parole con lunghezza compresa tra 3 e 6 caratteri.\nPremi invio per usare l'intero dizionario",
		'insert_min_max': "Minimo.Massimo: ",
		'not_numbers': "Non hai inserito numeri",
		'try_again': "Riprova",
		'filtering_range': "Filtrando parole che sono nel range {mn}/{mx} di lunghezza.",
		'confirm_word_count': "{word_count} parole, sei d'accordo? (y|n)> ",
		'custom_set_prompt': "Digita tutti i caratteri su cui vuoi esercitarti. (minimo 2). Riga vuota per procedere",
		'transmitting_exercise': "Esercizio di trasmissione.\nEcco una serie casuale di pseudo-call e numeri progressivi,\n\tprova a trasmetterli con il tuo tasto CW preferito senza errori.\nQualsiasi tasto per passare al successivo, ESC per terminare l'esercizio.",
		'press_any_key': "Premi un tasto quando sei pronto per iniziare.",
		'bye_message': "Ciao per ora. Torniamo al menu principale.",
		'counting_prompt': "Conteggio, SÌ o NO?\nBarra spaziatrice significa: gruppo ricevuto;\nQualsiasi altro tasto significa: gruppo perso;\nPremi ESC per tornare al menu principale.",
		'exercise_number': "Esercizio numero {esnum}:",
		'total_correct': "\nTotale: {cont}, corrette: {corr}, errori(%): {pde:.2f}%.",
		'passed': "Superato!",
		'failed': "Fallito: {difference:.2f}% oltre la soglia.",
		'report_saved': "Rapporto salvato su CW_Diary.txt",
		'note_on_exercise': "\nNota su questo esercizio: ",
		'empty_note': "Nota: nessuna",
		'groups_received_few': "Gruppi ricevuti {cont} su 100: esercizio non salvato su disco.",
		'session_saved': "Sessione {session_number}, durata: {duration} è stata salvata su disco.",
		'menu_main': {
			"c": "Risultati conteggio",
			"k": "Tastiera ed impostazioni CW",
			"l": "Ascolta gli appunti in CW",
			"m": "Mostra Menu",
			"q": "Per uscire da questa app",
			"r": "Esercizio di ricezione",
			"t": "Esercizio di trasmissione",
			"w": "Crea dizionario personalizzato",
			"z": "Scegli la lingua dell'applicazione"
		},
		'menu_rx': {
			"1": "Pseudo-call",
			"2": "Gruppi o parole"
		},
		'menu_rx_kind': {
			"1": "Solo lettere (A a Z)",
			"2": "Solo numeri (0 a 9)",
			"3": "Lettere e numeri (A a Z e 0 a 9)",
			"4": "Set personalizzato (decidi quali simboli vuoi usare)",
			"5": "Parole (dal tuo dizionario personale)"
		},
		'select_exercise': "Ora seleziona quale esercizio vuoi fare:",
		'please_just_1_or_2': "Per favore, solo 1 o 2",
		'choose_a_number': "Scegli un numero per favore",
		'give_length': "Dammi la lunghezza del gruppo tra 1 e 7: ",
		'filter_words_set': "\nFiltriamo il set di parole da usare con l'esercizio\nPer favore, digita la lunghezza minima.massima delle parole che vuoi scegliere casualmente. Es. 3.6\nsceglierà parole con lunghezza compresa tra 3 e 6 caratteri.\nPremi invio per usare l'intero dizionario",
		'careful_type': "Fai molta attenzione adesso.\n\tDigita il {kindstring} che ascolti.\nBattendo invio a vuoto (o aggiungendo un ?) avrai l'opportunità di un secondo tentativo\n\tPer terminare: digita semplicemente un '.' (punto) seguito da dal tasto invio.\n\t\tBUON DIVERTIMENTO!\n\tPremi un tasto quando sei pronto per iniziare.",
		'begin_session': "Iniziamo la sessione {sessions}!",
		'over_check': "È finita! Ora vediamo cosa abbiamo ottenuto.",
		'received_too_few': "Hai ricevuto troppo pochi {kindstring} per generare statistiche consistenti.",
		'time_to_receive': "\nE' il momento giusto per un bell'esercizio di ricezione? Ottimo, allora sei nel posto giusto.\nIniziamo!\n\tCarico lo stato dei tuoi progressi e controllo il database del dizionario...",
		'dictionary_loaded': "Dizionario delle parole caricato con {word_count} parole.",
		'file_not_found': "File words.txt non trovato. Fornisci un file di dizionario: 1 parola per linea.",
		'first_class': "Ops, questa è probabilmente la tua prima lezione. Sto creando il record.",
		'got_data': "Ho recuperato i tuoi dati dal disco, quindi:\nLa tua attuale velocità WPM è {wpm} e hai svolto {sessions} sessioni.\nTi ho inviato {totalcalls} pseudo-call o gruppi e ne hai ricevuti correttamente {totalget}, mentre {totalwrong} li hai copiati male.\nIl tempo totale speso su questo esercizio è stato di {totaltime}.",
		'set_wpm': "Vuoi cambiare la velocità in WPM? Invio per accettare {wpm}> ",
		'empty_clipboard': "vuoti",
		'not_a_command': "Non è un comando!",
		'press_m_for_menu': "\nCWAPU - VERSIONE: {version} DI GABRY - IZ4APU.\n\t----UTILITÀ PER IL TUO CW----\n\t\tPremi 'm' per il menu.",
		'o_set_loaded':"Impostazioni generali caricate",
		'o_set_created':"Impostazioni generali di default",
		'o_set_saved':"Impostazioni generali salvate sul disco.",
		'l_set':"Lingua dell'applicazione impostata su Italiano",
		'not_a_valid_language': "Lingua non valida",
		'counting_exercise_report': "Esercizio di conteggio #{esnum} eseguito il {date} alle {time} minuti:\n",
		'total_correct_report': "Totale: {cont}, corrette: {corr}, errori(%): {pde:.2f}%.\n",
		'note_with_text': "Nota: {nota}\n***\n",
		'session_summary': "In questa sessione #{sessions}, ti ho inviato {calls} {kindstring} e ne hai ricevuti {callsget_len}: {percentage:.1f}%",
		'first_shot': "\t{first_shot} di questi sono stati ricevuti al primo ascolto: {first_shot_percentage:.1f}%",
		'with_repetition': "\tmentre {repetitions} {kindstring} al secondo tentativo: {repetitions_percentage:.1f}%.",
		'speed_summary': "Durante la sessione, la tua velocità minima è stata {minwpm}, la massima di {maxwpm}: pari ad una variazione di {range_wpm} WPM.\n\tLa velocità media di ricezione è di: {average_wpm:.1f} WPM.",
		'character_mistakes': "Carattere: errori = Percentuale",
		'total_mistakes': "\nErrori totali: {global_mistakes} su {send_char} = {mistake_percentage:.2f}%",
		'never_misspelled': "\nCaratteri mai sbagliati: {good_letters}",
		'how_many': "\nQuanti ne vuoi ricevere? (INVIO per infinito)> ",
		'no_mistakes_recorded': "Nessun errore sui caratteri registrato in questa sessione.",
		'fix_yes': "Vuoi che il cw rimanga alla stessa velocità?	(y|n)> ",
		'h_keyboard':
			"Benvenuto nella sezione dove potrai ascoltare il CW e configurare tutti i suoi parametri.\nQuesti parametri saranno validi e attivi in tutto CWAPU e verranno salvati automaticamente quando esci dall'app.\nOra, leggi attentamente quanto segue:\n" \
			"tPremi Invio senza digitare nulla per uscire e tornare al menu principale;\n" \
			"\tdigita .w seguito da un valore numerico per impostare il WPM;\n"\
			"\tdigita .h seguito da un valore per il pitch del picco della nota CW che vuoi usare;\n"\
			"\tdigita .l seguito da un valore per impostare la linea, il default è 30;\n"\
			"\tdigita .s seguito da un valore per impostare lo spazio, il default è 50;\n"\
			"\tdigita .p proprio come .s ma per i punti;\n"\
			"\tdigita .v seguito da un valore tra 0 e 100 per impostare il volume;\n"\
			"\tdigita .f1 .f2 .f3 o .f4 per cambiare la forma d'onda;\n"\
			"\tdigita .m seguito da millisecondi per impostare il fade in e out per la nota CW;\n"\
			"\tdigita .g seguito da un valore per impostare la quantità di esercizi per le statistiche globali;\n"\
			"\tdigita .x seguito da un valore per impostare ogni quanti caratteri aggiornare le stats globali;\n"\
			"\tdigita .t #-# dove i # sono i valori minimo-massimo del filtro per la scelta delle parole;\n"\
			"\tdigita .y per impostare un gruppo personalizzato di caratteri su cui allenarti;\n"\
			"\tdigita .sr per impostare il sample rate da inviare alla tua scheda audio;\n"\
			"\tdigita ? per vedere questo messaggio di aiuto;\n"\
			"\tdigita ?? per visualizzare i parametri impostati;\n"\
			"\tdigita .rs per reimpostare il CW al peso standard di 1/3\n"\
			"\tdigita .sv <testo> per salvare il CW in un file .wav\n",
		'generating_historical_report':"Generazione report storico in corso...",
		'no_historical_data_to_report':"Nessun dato salvato disponibile per il report.",
		'no_sessions_in_current_block_for_report':"Nessuna sessione nel blocco corrente da riportare.",
		'historical_report_saved_to':"Report storico salvato in: {filename}",
		'error_saving_historical_report':"Errore durante il salvataggio del report storico {filename}: {e}",
		'unexpected_error_generating_report':"Errore imprevisto durante la generazione del report: {e}",
		'report_header_appname': "CWAPU", # Puoi personalizzare se preferisci
		'historical_stats_report_title': "Report Statistiche Storiche Esercizi Rx",
		'report_generated_on': "Report generato il",
		'stats_based_on_exercises': "Statistiche basate su {count} esercizi",
		'overall_speed_stats': "Statistiche Velocità Complessive",
		'min_wpm': "WPM Min",
		'max_wpm': "WPM Max",
		'avg_wpm_cpm_based': "WPM Medio (su CPM)",
		'overall_error_stats': "Statistiche Errori Complessive",
		'total_chars_sent_in_block': "Caratteri totali inviati (nel blocco)",
		'total_errors_in_block': "Errori totali (nel blocco)",
		'error_details_by_char': "Dettaglio errori per carattere",
		'of_total_chars': "dei car. tot.", # Abbreviato per brevità, o "dei caratteri totali"
		'variations_from_previous_block': "Variazioni Rispetto al Blocco Precedente",
		'exercises_articles': "esercizi", # Usato come: {count} esercizi
		'vs': "vs.", # O "contro"
		'change': "Variazione",
		'overall_error_rate': "Tasso errore generale",
		'error_details_variations': "Variazioni Dettaglio Errori per Carattere",
		'no_errors_in_either_block': "Nessun errore registrato in nessuno dei due blocchi di riferimento.",
		'rate_change_char': "Variaz. tasso",
		'avg_wpm_of_session_avgs_label':"WPM Medio (media delle sessioni)",
		'graphical_report_saved_to':"Report grafico salvato in: {filename}",
		'error_generating_graphical_report: ':"Errore durante il salvataggio del report grafico: {error}",
		'error_saving_graphical_file: ':"Errore durante il salvataggio del file grafico {filename}: {error}",
		'of_specific_char_sent':"delle '{char_upper}' inviate",
		'error_detail_line_format':"'{char_upper}': {count} ({perc_vs_total:.2f}% {of_total_chars_label}, {perc_vs_specific:.2f}% {of_specific_char_sent_label})",
		'rate_change_specific_char':"Variaz. tasso (su '{char_upper}' inv.)",
		'delta_rate_total_label': "Δ Tasso (vs tot):",
		'delta_rate_specific_label': "Δ Tasso (vs '{char_upper}' inv.):",
		'metric': "Metrica",
		'current_value': "Valore Attuale",
		'previous_value': "Valore Precedente",
		'error_count_header': "N. Errori",
		'perc_vs_total_chars_header': "% su Tot. Caratt.",
		'perc_vs_spec_char_header': "% su Caratt. Spec. Inv.", # Leggermente più esplicito
		'of_specific_char_sent_count': "su {count} '{char_upper}' inv.",
		'variations_vs_block_of': "Variazioni rispetto al blocco di {count} esercizi precedente",
		'curr_error_count_header': "Err. Att.",
		'curr_perc_vs_total_header': "%Tot Att.",
		'curr_perc_vs_spec_header': "%Spec Att.",
		'prev_error_count_header': "Err. Prec.",
		'prev_perc_vs_total_header': "%Tot Prec.",
		'prev_perc_vs_spec_header': "%Spec Prec.",
		'delta_rate_total_header': "Δ% Tot. Caratt.",
		'delta_rate_spec_header': "Δ% Caratt. Spec.",
		'of_n_sent': "su {count} inv.",
		'delta_rate_total_label': "Δ Tasso (vs tot. caratt.):",
		'delta_rate_specific_label': "Δ Tasso (vs '{char_upper}' inv.):",
		'no_detailed_errors_to_display': "Nessun errore di dettaglio da visualizzare nel grafico.",
		'no_errors_recorded_for_block': "Nessun errore registrato per questo blocco di sessioni.",
		'visualization_to_be_implemented': "Visualizzazione da implementare",
		'delta_rate_specific_label_short': "Variaz. % Err. Spec.",
		'no_error_variations_to_display': "Nessuna variazione significativa degli errori per carattere da visualizzare.",
		'no_previous_data_for_variations': "Dati precedenti non disponibili per calcolare le variazioni.",
		'custom_set_use_prefill_prompt': "Vuoi iniziare con un gruppo di caratteri precompilato?",
		'no_key_default': "n",
		'custom_set_prefilled_with_errors': "Gruppo precompilato con errori frequenti: {chars}",
		'custom_set_prefilled_with_random': "Gruppo precompilato con caratteri casuali: {chars}",
		'custom_set_prefill_failed_no_chars': "Impossibile precompilare: nessun carattere valido disponibile.",
		'custom_set_modify_prompt_intro': "Inserisci/modifica caratteri (toggle). Invio per terminare.",
		'yes_key_default': "s",
		'invoking_custom_set_editor': "Avvio editor gruppo Custom...",
		'custom_set_updated_short_feedback': "Set custom: {num_chars} car.", # Per feedback comando .y
		'menu_rx_switcher_parole': "Parole",
		'menu_rx_switcher_lettere': "Lettere",
		'menu_rx_switcher_numeri': "Numeri",
		'menu_rx_switcher_simboli': "Simboli",
		'menu_rx_switcher_qrz': "QRZ",
		'menu_rx_switcher_custom': "Custom",
		'switcher_status_on_label': "ATTIVATO",
		'switcher_status_off_label': "disattivato",
		'rx_switcher_menu_title': "Esercizi Rx - Seleziona Tipi (Invio per iniziare):",
		'rx_switcher_menu_prompt': "Scegli (1-6) o Invio: ",
		'rx_switcher_no_selection_error': "Nessuna modalità di esercizio selezionata! Attiva almeno uno switcher.",
		'rx_switcher_group_length_prompt': "Lunghezza gruppi (1-7 per Lettere/Numeri/Simboli/Custom):",
		'rx_switcher_invalid_length_error': "Lunghezza non valida. Inserire un numero da 1 a 7.",
		'parole_filter_no_results_with_saved': "Filtro parole caricato dalle impostazioni non ha prodotto risultati. Switcher 'Parole' disattivato.",
		'parole_filter_use_dot_command': "Filtro parole non impostato/valido. Usa il comando '.t #-#' nelle Impostazioni (k). Switcher 'Parole' disattivato.",
		'parole_filter_applied_from_settings': "Filtro parole applicato dalle impostazioni ({count} parole).",
		'custom_set_invoking': "Avvio configurazione gruppo personalizzato...",
		'custom_set_not_created_deactivating': "Gruppo Custom non creato o non valido. Switcher 'Custom' disattivato.",
		'custom_set_loaded_from_settings': "Gruppo Custom caricato dalle impostazioni: [{set_string}]",
		'invalid_menu_choice': "Scelta non valida.",
		'parole_filter_not_set_error': "Errore: 'Parole' attivo ma il filtro non è impostato o non produce risultati. Usa '.t #-#'.",
		'mixed_exercise_types_label': "Misto ({types})",
		'error_no_item_generated_rx': "Errore: Impossibile generare item per l'esercizio con le selezioni attuali. Controlla le impostazioni del menu Rx.",
		'chars_to_next_report_progress': "Completamento sezione corrente:\n+{s} -> ({x} / {y}) = {z}% (-{w}) alla prossima generazione.",
		'reports_disabled': "La generazione automatica dei report è disabilitata."
		#Qit
	}
}
