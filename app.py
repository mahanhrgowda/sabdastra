import streamlit as st
import random  # For randomizing quizzes

# Session state for tracking progress, XP, and quests
if 'progress' not in st.session_state:
    st.session_state.progress = {
        'level1': False,
        'level2': False,
        'level3': False,
        'level4': False,
        'level5': None,  # Will be the chosen path
        'level6': False,
        'advanced_mantras': False,
        'vedic_math': False,
        'yoga_sutras': False,
        'bhagavad_gita': False,
        'maheshwara_sutras': False,
        'panini_grammar': False
    }
if 'xp' not in st.session_state:
    st.session_state.xp = 0
if 'quests' not in st.session_state:
    st.session_state.quests = {
        'quest1': {'name': 'Sound Explorer', 'completed': False, 'xp': 50, 'desc': 'Learn basic Sanskrit sounds.'},
        'quest2': {'name': 'Command Caster', 'completed': False, 'xp': 75, 'desc': 'Cast your first command.'},
        'quest3': {'name': 'Bhāva Weaver', 'completed': False, 'xp': 100, 'desc': 'Infuse emotions into commands.'},
        'quest4': {'name': 'Grammar Guardian', 'completed': False, 'xp': 150, 'desc': 'Forge grammar rules.'},
        'quest5': {'name': 'Pattern Pro', 'completed': False, 'xp': 200, 'desc': 'Cast complex patterns.'},
        'quest6': {'name': 'Chakra Connector', 'completed': False, 'xp': 250, 'desc': 'Channel chakras with mantras.'},
        'quest7': {'name': 'Shield Master', 'completed': False, 'xp': 300, 'desc': 'Activate defenses using protective mantras.'},
        'quest8': {'name': 'Path Pioneer', 'completed': False, 'xp': 500, 'desc': 'Choose and complete a path.'},
        'quest9': {'name': 'Phonetics Sage', 'completed': False, 'xp': 400, 'desc': 'Master Sanskrit phonetics.'},
        'quest10': {'name': 'Mantra Mystic', 'completed': False, 'xp': 350, 'desc': 'Chant advanced Sanskrit mantras.'},
        'quest11': {'name': 'Vedic Math Wizard', 'completed': False, 'xp': 450, 'desc': 'Solve problems using Vedic math techniques.'},
        'quest12': {'name': 'Sutra Scholar', 'completed': False, 'xp': 500, 'desc': 'Explore and interpret key Yoga Sutras.'},
        'quest13': {'name': 'Gita Guide', 'completed': False, 'xp': 500, 'desc': 'Explore key Bhagavad Gita verses.'},
        'quest14': {'name': 'Maheshwara Master', 'completed': False, 'xp': 400, 'desc': 'Explore the Maheshwara Sutras and Sanskrit phonemes.'},
        'quest15': {'name': 'Panini Grammarian', 'completed': False, 'xp': 450, 'desc': 'Explore Panini\'s Ashtadhyayi grammar concepts.'}
    }
if 'sanskrit_phonetics' not in st.session_state:
    st.session_state.sanskrit_phonetics = False  # Track phonetics section

# XP thresholds for levels (cumulative)
xp_thresholds = [0, 100, 300, 600, 1000, 1500, 2500, 3000, 3500, 4000, 4500, 5000, 5450]  # Extended

# Function to award XP and check quests
def award_xp(quest_key):
    if not st.session_state.quests[quest_key]['completed']:
        st.session_state.xp += st.session_state.quests[quest_key]['xp']
        st.session_state.quests[quest_key]['completed'] = True
        st.success(f"Quest '{st.session_state.quests[quest_key]['name']}' completed! +{st.session_state.quests[quest_key]['xp']} XP")
        check_level_progress()

# Check if XP unlocks next level/section
def check_level_progress():
    current_xp = st.session_state.xp
    if current_xp >= xp_thresholds[1] and not st.session_state.progress['level1']:
        st.session_state.progress['level1'] = True
    if current_xp >= xp_thresholds[2] and not st.session_state.progress['level2']:
        st.session_state.progress['level2'] = True
    if current_xp >= xp_thresholds[3] and not st.session_state.progress['level3']:
        st.session_state.progress['level3'] = True
    if current_xp >= xp_thresholds[4] and not st.session_state.progress['level4']:
        st.session_state.progress['level4'] = True
    if current_xp >= xp_thresholds[5] and st.session_state.progress['level5'] is not None and not st.session_state.progress['level6']:
        st.session_state.progress['level6'] = True
    if current_xp >= xp_thresholds[6] and not st.session_state.progress['advanced_mantras']:
        st.session_state.progress['advanced_mantras'] = True
    if current_xp >= xp_thresholds[7] and not st.session_state.progress['vedic_math']:
        st.session_state.progress['vedic_math'] = True
    if current_xp >= xp_thresholds[8] and not st.session_state.progress['yoga_sutras']:
        st.session_state.progress['yoga_sutras'] = True
    if current_xp >= xp_thresholds[9] and not st.session_state.progress['bhagavad_gita']:
        st.session_state.progress['bhagavad_gita'] = True
    if current_xp >= xp_thresholds[10] and not st.session_state.progress['maheshwara_sutras']:
        st.session_state.progress['maheshwara_sutras'] = True
    if current_xp >= xp_thresholds[11] and not st.session_state.progress['panini_grammar']:
        st.session_state.progress['panini_grammar'] = True

# Modularized parsers for Śabdāstra interpreter
def parse_sutra(code):
    sutra_num = code.split("(")[1].split(")")[0].strip("'\"")
    sutras_dict = {
        "1.1": {"sanskrit": "atha yoga anushasanam", "translation": "Now, the teachings of yoga.", "explanation": "The beginning of the text, introducing the study of Yoga."},
        "1.2": {"sanskrit": "yogas citta-vrtti-nirodhah", "translation": "Yoga is the control of the mind.", "explanation": "Yoga calms the mind by quieting distractions and stresses; it reduces stress in life."},
        "1.3": {"sanskrit": "tada drashtuh svarupe avasthanam", "translation": "Then the Seer abides in its own nature.", "explanation": "When the mind is still, the true self is revealed."},
        "1.4": {"sanskrit": "vrtti sarupyam itaratra", "translation": "At other times, the seer identifies with the fluctuating consciousness.", "explanation": "When the mind is not controlled, we identify with thoughts and emotions."},
        "1.5": {"sanskrit": "vrttayah pancatayyah klista aklistah", "translation": "The vrttis are five-fold, afflicted or unafflicted.", "explanation": "Mental modifications can cause suffering or not."},
        "1.13": {"sanskrit": "tatra sthitau yatno ‘bhyâsah", "translation": "Practice means choosing, applying the effort, and doing those actions that bring a stable and tranquil state.", "explanation": "Practice extends tranquility beyond the mat to daily life for contentment."},
        "1.14": {"sanskrit": "sa tu dîrgha-kâla-nairantarya-satkârâsevito drdha-bhûmih", "translation": "When this practice is done for a long time, and with sincere devotion, then the practice becomes a firmly rooted, stable, and solid foundation.", "explanation": "Regular practice builds a solid foundation for growth."},
        "1.27": {"sanskrit": "tasya vâcakah prañavah", "translation": "Isvara is the Sanskrit word for pure awareness, and is represented by the sound of OM, the universal vibration that connects us all.", "explanation": "OM represents pure awareness and the source of knowledge and creativity."},
        "1.34": {"sanskrit": "pracchardana-vidhârañâbhyâm vâ prâñasya", "translation": "The mind is also calmed by regulating the breath, particularly attending to the exhalation and the natural stilling of breath that comes from such practice.", "explanation": "Breath regulation calms the mind and body in stressful situations."},
        "2.1": {"sanskrit": "tapah-svâdhyâyesvara-prañidhânâni kriyâ-yogah", "translation": "Yoga in the form of action has three parts: 1. Training and purifying the senses, 2. Self-study in the context of teachings, 3. Devotion and tapping into the creative source from which we emerged.", "explanation": "Yoga is a full mind-spirit-body practice beyond physical poses."},
        "2.3": {"sanskrit": "avidya asmita raga dvesa abhinivesah klesah", "translation": "The five afflictions are ignorance, egoism, attachment, aversion, and clinging to life.", "explanation": "These are the root causes of suffering."},
        "2.15": {"sanskrit": "parinama tapa samskara duhkhair guna vrtti virodhac ca duhkham eva sarvam vivekinah", "translation": "To the enlightened, all is suffering due to change, anxiety, and conditioning.", "explanation": "Even pleasure leads to suffering for the wise."},
        "2.28": {"sanskrit": "yogângânusthânâd asuddhi-ksaye jnâna-dîptir âviveka-khyâteh", "translation": "Through the practice of the different limbs (or steps) of a complete yoga practice, whereby impurities are eliminated, there arises an illumination that culminates in discriminative wisdom or enlightenment.", "explanation": "Practicing the eight limbs leads to self-knowledge, contentment, and fulfillment."},
        "2.29": {"sanskrit": "yama-niyamâsana-prâñâyâma-pratyâhâra-dhârañâ-dhyâna-samâdhayo ‘stâv angâni", "translation": "The eight limbs of yoga are the codes of self-regulation or restraint, observances or practices of self-training, postures, expansion of breath and prana, withdrawal of the senses, concentration, meditation, and perfected concentration.", "explanation": "The eight limbs include more than postures; all aspects should be valued."},
        "2.30": {"sanskrit": "ahimsâ-satyâsteya-brahmacaryâparigrahâ yamâh", "translation": "Non-injury or non-harming, truthfulness, abstention from stealing, and non-possessiveness or non-attachment are the five Yamas, or codes of self-regulation. The Yamas are the first of the eight steps of yoga.", "explanation": "The Yamas promote kindness and positive impact, allowing self-defense."},
        "2.31": {"sanskrit": "ete jâti-desa-kâla-samayânavacchinnâh sârva-bhaumâ mahâvratam", "translation": "These codes of self-regulation become a powerful standard to live by when they can be practiced unconditionally.", "explanation": "Practice the Yamas from compassion toward all."},
        "2.32": {"sanskrit": "sauca-santosa-tapah-svâdhyâyesvara-prañidhânâni niyamâh", "translation": "Cleanliness and purity of body and mind, an attitude of contentment, discipline, self-study and reflection on sacred words, and an attitude of surrender are the observances or practices of self-training, and are the second rung on the ladder of yoga, otherwise known as the Niyamas.", "explanation": "The Niyamas guide self-care and higher awareness."},
        "2.46": {"sanskrit": "sthira-sukham âsanam", "translation": "The means of perfecting the posture is that of relaxing, relenting effort, and allowing your attention to merge with endlessness, or the infinite.", "explanation": "Asana focuses on steadiness and ease, not flexibility."},
        "2.49": {"sanskrit": "tasmin sati svâsa-prasvâsayor gati-vicchedah prâñâyâmah", "translation": "Once a posture has been achieved, you will begin to incorporate breath control, or pranayama. Breath regulation is the fourth of the eight rungs.", "explanation": "Breath control integrates with asana for complete practice."},
        "2.54": {"sanskrit": "sva-visayâsamprayoge cittasya svarûpânukâra ivendriyânam pratyâhârah", "translation": "When your own senses and actions cease to be engaged with the corresponding objects in your mental realm, and withdraw into the consciousness from which they arose, this is called Pratyahara, the fifth step.", "explanation": "Pratyahara withdraws senses to understand unique perception."},
        "3.1": {"sanskrit": "desa-bandhas cittasya dhârañâ", "translation": "Concentration is the process of holding or fixing the mind’s attention onto one object or place, and is the sixth of the eight rungs.", "explanation": "Concentration builds discipline, focus, and reduces stress."},
        "3.2": {"sanskrit": "tatra pratyayaika-tânatâ dhyânam", "translation": "The repeated continuation, or uninterrupted stream of that one point of focus is called absorption in meditation, and is the seventh of the eight steps.", "explanation": "Meditation grows understanding in yoga practice."},
        "3.3": {"sanskrit": "tad evârtha-mâtra-nirbhâsam svarûpa-sûnyam iva samâdhih", "translation": "When only the essence of that object, place, or point of focus shines forth in the mind, that deep concentration is called Samadhi, which is the eighth rung.", "explanation": "Samadhi leads to new thinking and self-revelations."},
        "3.49": {"sanskrit": "tato mano-javitvam vikaraña-bhâvah pradhâna-jayas ca", "translation": "With mastery over the senses, thoughts, and actions comes quickness of mind and perception.", "explanation": "Mastery brings contentment in life and practice."},
        "4.1": {"sanskrit": "janma ausadhi mantra tapah samadhi jah siddhayah", "translation": "Psychic powers arise by birth, drugs, incantations, self-discipline or samadhi.", "explanation": "Siddhis can come from various means, but samadhi is the highest."},
        "4.15": {"sanskrit": "vastu-sâmye citta-bhedât tayor vibhaktah panthâh", "translation": "Although individuals perceive the same objects, these objects are perceived in different ways, because those minds are each unique and beautifully diverse.", "explanation": "Respect unique perceptions of the world."},
        "4.31": {"sanskrit": "tadâ sarvâvaraña-malâpetasya jnânasyânantyâj jneyam alpam", "translation": "Then, by the removal of the layers of imperfection, there comes the experience of the infinite, along with the realization that knowledge is infinite.", "explanation": "Practice removes impurities, leading to enlightenment and infinite wisdom."},
        "4.34": {"sanskrit": "purusartha sunyanam gunanam pratiprasavah kaivalyam svarupa pratistha va citi saktir iti", "translation": "Kaivalya is the establishment of the power of consciousness in its own nature.", "explanation": "Ultimate liberation is realizing the true self beyond the gunas."}
    }
    sutra = sutras_dict.get(sutra_num)
    if sutra:
        return f"Sutra {sutra_num}: {sutra['sanskrit']}\nTranslation: {sutra['translation']}\nExplanation: {sutra['explanation']}"
    return "Unknown sutra. Try '1.2' or others from the list."
# Bhagavad Gita verses
elif code.startswith("gita_read("):
    gita_num = code.split("(")[1].split(")")[0].strip("'\"")
    gita_dict = {
        "1.1": {"sanskrit": "dhṛtarāṣṭra uvāca dharma-kṣetre kuru-kṣetre samavetā yuyutsavaḥ māmakāḥ pāṇḍavāś caiva kim akurvata sañjaya", "translation": "Dhritarashtra said: O Sanjay, after gathering on the holy field of Kurukshetra, and desiring to fight, what did my sons and the sons of Pandu do?", "explanation": "The opening verse sets the scene of the battlefield."},
        "2.47": {"sanskrit": "karmaṇy evādhikāras te mā phaleṣu kadācana mā karma-phala-hetur bhūr mā te saṅgo ’stv akarmaṇi", "translation": "You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions.", "explanation": "Focus on action without attachment to results."},
        "2.14": {"sanskrit": "mātrā-sparśās tu kaunteya śītoṣṇa-sukha-duḥkha-dāḥ āgamāpāyino ’nityās tāṁs titikṣasva bhārata", "translation": "O son of Kunti, the nonpermanent appearance of happiness and distress, and their disappearance in due course, are like the appearance and disappearance of winter and summer seasons. They arise from sense perception, and one must learn to tolerate them without being disturbed.", "explanation": "Endure dualities with equanimity."},
        "3.21": {"sanskrit": "yad yad ācarati śreṣṭhas tat tad evetaro janaḥ sa yat pramāṇaṁ kurute lokas tad anuvartate", "translation": "Whatever action a great man performs, common men follow. And whatever standards he sets by exemplary acts, all the world pursues.", "explanation": "Leaders set examples for others."},
        "4.7": {"sanskrit": "yadā yadā hi dharmasya glānir bhavati bhārata abhyutthānam adharmasya tadātmānaṁ sṛjāmy aham", "translation": "Whenever and wherever there is a decline in religious practice, O descendant of Bharata, and a predominant rise of irreligion—at that time I descend Myself.", "explanation": "God incarnates to protect dharma."},
        "5.21": {"sanskrit": "bāhya-sparśeṣv asaktātmā vindaty ātmani yat sukham sa brahma-yoga-yuktātmā sukham akṣayam aśnute", "translation": "Such a liberated person is not attracted to material sense pleasure but is always in trance, enjoying the pleasure within. In this way the self-realized person enjoys unlimited happiness, for he concentrates on the Supreme.", "explanation": "True happiness comes from within."},
        "9.26": {"sanskrit": "patraṁ puṣpaṁ phalaṁ toyaṁ yo me bhaktyā prayacchati tad ahaṁ bhakty-upahṛtam aśnāmi prayatātmanaḥ", "translation": "If one offers Me with love and devotion a leaf, a flower, a fruit or water, I will accept it.", "explanation": "Devotion is key in offerings to God."},
        "12.5": {"sanskrit": "kleśo ’dhikataras teṣām avyaktāsakta-cetasām avyaktā hi gatir duḥkham dehavadbhir avāpyate", "translation": "For those whose minds are attached to the unmanifested, impersonal feature of the Supreme, advancement is very troublesome. To make progress in that discipline is always difficult for those who are embodied.", "explanation": "Devotion to the personal form is easier."},
        "18.66": {"sanskrit": "sarva-dharmān parityajya mām ekaṁ śaraṇaṁ vraja ahaṁ tvā sarva-pāpebhyo mokṣayiṣyāmi mā śucaḥ", "translation": "Abandon all varieties of dharma and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear.", "explanation": "Ultimate surrender to God liberates."},
        "2.20": {"sanskrit": "na jāyate mriyate vā kadācin nāyaṁ bhūtvā bhavitā vā na bhūyaḥ ajo nityaḥ śāśvato ’yaṁ purāṇo na hanyate hanyamāne śarīre", "translation": "For the soul there is neither birth nor death at any time. He has not come into being, does not come into being, and will not come into being. He is unborn, eternal, ever-existing and primeval. He is not slain when the body is slain.", "explanation": "The soul is eternal and indestructible."},
        "4.11": {"sanskrit": "ye yathā māṁ prapadyante tāṁs tathaiva bhajāmy aham mama vartmānuvartante manuṣyāḥ pārtha sarvaśaḥ", "translation": "As all surrender unto Me, I reward them accordingly. Everyone follows My path in all respects, O son of Pṛthā.", "explanation": "God responds to devotion in kind."},
        "6.5": {"sanskrit": "uddhared ātmanātmānaṁ nātmānam avasādayet ātmaiva hy ātmano bandhur ātmaiva ripur ātmanaḥ", "translation": "One must deliver himself with the help of his mind, and not degrade himself. The mind is the friend of the conditioned soul, and his enemy as well.", "explanation": "Master your mind to elevate yourself."},
        "9.34": {"sanskrit": "man-manā bhava mad-bhakto mad-yājī māṁ namaskuru mām evaiṣyasi yuktvaivam ātmānaṁ mat-parāyaṇaḥ", "translation": "Engage your mind always in thinking of Me, become My devotee, offer obeisances to Me and worship Me. Being completely absorbed in Me, surely you will come to Me.", "explanation": "Devotional service leads to God."},
        "18.65": {"sanskrit": "man-manā bhava mad-bhakto mad-yājī māṁ namaskuru mām evaiṣyasi satyaṁ te pratijäne priyo ’si me", "translation": "Always think of Me, become My devotee, worship Me and offer your homage unto Me. Thus you will come to Me without fail. I promise you this because you are My very dear friend.", "explanation": "God's promise to devotees."}
    }
    gita = gita_dict.get(gita_num)
    if gita:
        return f"Gita {gita_num}: {gita['sanskrit']}\nTranslation: {gita['translation']}\nExplanation: {gita['explanation']}"
    return "Unknown Gita verse. Try '2.47' or others from the list."
# Expanded Sanskrit phonetics
elif code.startswith("phonetic_read("):
    sound = code.split("(")[1].split(")")[0].strip("'\"").lower()
    phonetics_dict = {
        "a": "Short a [ɐ], open central vowel, like in 'comma'. Represents creation and unity. 🌟",
        "aa": "Long ā [aː], open back vowel, like in 'bra'. Prolonged sound of a.",
        "i": "Short i [i], close front vowel, like in 'sit'. Focus and intention. 🔍",
        "ii": "Long ī [iː], like in 'feet'. Prolonged i.",
        "u": "Short u [u], close back vowel, like in 'full'. Flow and movement. 🌊",
        "uu": "Long ū [uː], like in 'fool'. Prolonged u.",
        "e": "Long e [eː], close-mid front vowel, like Scottish 'wait'.",
        "o": "Long o [oː], close-mid back vowel, like in 'story'.",
        "ai": "Diphthong ai [ɐːi̯], like in 'eye'.",
        "au": "Diphthong au [ɐːu̯], like in 'out'.",
        "r": "Ṛ [r̩], syllabic r, like in 'bird' (American English).",
        "rr": "Ṝ [r̩ː], longer ṛ.",
        "l": "Ḷ [l̩], syllabic l, like in 'bottle'.",
        "ll": "Ḹ [l̩ː], longer ḷ.",
        "k": "Ka [k], voiceless velar stop, like 'skin'. Guttural, sharp energy! 🗡️",
        "kh": "Kha [kʰ], aspirated k, like 'kin'.",
        "g": "Ga [ɡ], voiced velar stop, like 'again'.",
        "gh": "Gha [ɡʱ], aspirated g.",
        "ng": "Ṅa [ŋ], velar nasal, like 'sting'.",
        "c": "Ca [tɕ], voiceless palatal affricate, like 'riches' (palatalized).",
        "ch": "Cha [tɕʰ], aspirated c, like 'chew'.",
        "j": "Ja [dʑ], voiced palatal affricate, like 'juice' (palatalized).",
        "jh": "Jha [dʑʱ], aspirated j.",
        "ny": "Ña [ɲ], palatal nasal, like 'canyon'.",
        "t": "Ṭa [ʈ], voiceless retroflex stop, like 'stable' (American).",
        "th": "Ṭha [ʈʰ], aspirated ṭ.",
        "d": "Ḍa [ɖ], voiced retroflex stop, like 'bird' (American).",
        "dh": "Ḍha [ɖʱ], aspirated ḍ.",
        "n": "Ṇa [ɳ], retroflex nasal, like 'burn' (American).",
        "ta": "Ta [t], voiceless dental stop, like 'stable'.",
        "tha": "Tha [tʰ], aspirated t, like 'table'.",
        "da": "Da [d], voiced dental stop, like 'width'.",
        "dha": "Dha [dʱ], aspirated d.",
        "na": "Na [n], dental nasal, like 'tenth'.",
        "p": "Pa [p], voiceless bilabial stop, like 'span'.",
        "ph": "Pha [pʰ], aspirated p, like 'pan'.",
        "b": "Ba [b], voiced bilabial stop, like 'about'.",
        "bh": "Bha [bʱ], aspirated b, like 'clubhouse'.",
        "m": "Ma [m], bilabial nasal, like 'much'. Nurturing vibe. 🌸",
        "y": "Ya [j], palatal approximant, like 'yak'.",
        "r": "Ra [r], alveolar trill or flap, like Indian 'roti'.",
        "l": "La [l], alveolar lateral, like 'leaf'.",
        "v": "Va [ʋ], labiodental approximant, between 'wine' and 'vine'.",
        "sh": "Śa [ɕ], voiceless palatal fricative, like 'sheep' (palatalized). Wisdom and clarity. 🦉",
        "ss": "Ṣa [ʂ], voiceless retroflex fricative, like 'worship' (American).",
        "s": "Sa [s], voiceless alveolar fricative, like 'soup'.",
        "h": "Ha [ɦ], voiced glottal fricative, like 'ahead'.",
        "am": "Aṃ [◌̃], anusvara, nasal vowel.",
        "ah": "Aḥ [ḥ], visarga, like 'head'."
    }
    return phonetics_dict.get(sound, "Unknown phonetic. Explore more! Try lowercase Roman transliterations like 'a', 'aa', 'k', 'kh', etc.")
# Advanced Mantras
elif code.startswith("mantra_chant("):
    mantra = code.split("(")[1].split(")")[0].strip("'\"")
    mantras_dict = {
        "gayatri": "Om Bhur Bhuvah Svah Tat Savitur Varenyam Bhargo Devasya Dhimahi Dhiyo Yo Nah Prachodayat. Meaning: We meditate on the divine light of the sun. ☀️ Benefits: Enhances wisdom and clarity.",
        "mahamrityunjaya": "Om Tryambakam Yajamahe Sugandhim Pushtivardhanam Urvarukamiva Bandhanan Mrityor Mukshiya Maamritat. Meaning: We worship the three-eyed one. 🛡️ Benefits: Healing and protection.",
        "om namah shivaya": "Om Namah Shivaya. Meaning: I bow to Shiva. 🕉️ Benefits: Balances the five elements.",
        "aing namah": "Aing Namah. Meaning: Seed mantra for Saraswati. 📚 Benefits: Enhances knowledge and creativity.",
        "om mani padme hum": "Om Mani Padme Hum. Meaning: The jewel is in the lotus. 💎 Benefits: Compassion and purification."
    }
    return mantras_dict.get(mantra, "Unknown mantra. Try 'gayatri' or 'mahamrityunjaya'.")
# Vedic Math functions
elif code.startswith("vedic_square("):
    try:
        num = int(code.split("(")[1].split(")")[0].strip("'\""))
        if num % 10 == 5:
            base = num // 10
            return f"Square of {num}: {(base * (base + 1)) * 100 + 25} (Using Vedic trick for numbers ending in 5.)"
        else:
            return "Vedic square trick works best for numbers ending in 5."
    except:
        return "Invalid number for Vedic square."
elif code.startswith("vedic_multiply("):
    try:
        parts = code.split("(")[1].split(")")[0].split(",")
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        base = 10
        diff_a = a - base
        diff_b = b - base
        cross = (a + diff_b) * base
        prod_diff = diff_a * diff_b
        return f"{a} * {b} = {cross + prod_diff} (Using Vedic near-base multiplication.)"
    except:
        return "Invalid numbers for Vedic multiply."
elif code.startswith("sound_read("):
    sound = code.split("(")[1].split(")")[0].strip("'\"")
    if sound == "ka":
        return "Sharp energy detected! 🗡️"
    elif sound == "ma":
        return "Nurturing vibe unlocked! 🌸"
    else:
        return "Unknown sound. Try 'ka' or 'ma'."
elif code.startswith("vakya("):
    parts = code.split("(")[1].split(")")[0].split(",")
    message = parts[0].strip("'\"")
    if len(parts) > 1:
        bhava = parts[1].strip("'\" ").replace("bhava=", "")
        if bhava == "courage":
            return f"**{message.upper()}** 🦁 (Infused with courage!)"
        elif bhava == "peace":
            return f"{message} 🌊 (Infused with peace.)"
    return f"{message} (Basic command executed.)"
elif code.startswith("grammar_forge("):
    return "Grammar rules forged! Order established. 🔨"
elif code.startswith("pattern_cast("):
    return "Pattern cast! Sequence repeating... 🔄"
elif code.startswith("chakra_channel("):
    chakra = code.split("(")[1].split(")")[0].strip("'\"")
    if chakra == "heart":
        return "Heart Chakra channeled: Compassion flows! ❤️"
    return "Chakra channeled! Energy balanced. 🌀"
elif code.startswith("mantra_shield("):
    mantra = code.split("(")[1].split(")")[0].strip("'\"") if "(" in code else ""
    if mantra:
        return f"Shield activated with {mantra}! Protected against chaos. 🛡️"
    return "Shield activated! Protected against chaos. 🛡️"
elif code.startswith("hash_seal("):
    return "Data sealed with sound-pattern! 🔒 Only the right mantra unlocks it."
elif code.startswith("shastra_core()"):
    return "Logic architecture built! New language designed. 🏗️"
elif code.startswith("rasa_harmony()"):
    return "Emotions harmonized! Balance restored. 🎶"
elif code.startswith("kaala_map()"):
    return "Timelines mapped! Future predicted. 🔮"
else:
    return "Invalid Śabdāstra command. Check your syntax!"

# Main app
st.title("Śabdāstra Adventure: Become a Word-Weapon Master! 🌟")
st.write("""
Welcome, young Word-Smith! Śabdāstra is a magical coding language that mixes sounds, feelings, and rules to create powerful 'word-weapons' – but only for good! 
Like in code.org, you'll unlock levels through puzzles, challenges, and quests. Earn XP to progress!
Now with Advanced Sanskrit Mantras, Vedic Mathematics, Yoga Sutras, Bhagavad Gita, Maheshwara Sutras, and Panini Grammar explorations! Mantras are integrated into select quests for enhanced power.
Use the sidebar to navigate. Let's turn words into wonders! 💻🕉️
""")

# Display XP and Quests in sidebar
st.sidebar.header("Your Stats")
st.sidebar.write(f"XP: {st.session_state.xp} / {xp_thresholds[-1]}")
st.sidebar.progress(st.session_state.xp / xp_thresholds[-1])
st.sidebar.header("Quests")
for quest in st.session_state.quests.values():
    status = "✅" if quest['completed'] else "❌"
    st.sidebar.write(f"{status} {quest['name']} ({quest['xp']} XP): {quest['desc']}")

# Sidebar navigation
pages = ["Home", "Sanskrit Phonetics", "Level 1: Basics", "Level 2: Core", "Level 3: Systems", "Level 4: Defense", "Level 5: Paths", "Level 6: Mastery", "Advanced Mantras", "Vedic Mathematics", "Yoga Sutras", "Bhagavad Gita", "Maheshwara Sutras", "Panini Grammar"]
if not st.session_state.sanskrit_phonetics:
    pages = pages[:2] + pages[3:] if "Sanskrit Phonetics" in pages else pages
if not st.session_state.progress['level1']:
    pages = pages[:3]
elif not st.session_state.progress['level2']:
    pages = pages[:4]
elif not st.session_state.progress['level3']:
    pages = pages[:5]
elif not st.session_state.progress['level4']:
    pages = pages[:6]
elif st.session_state.progress['level5'] is None:
    pages = pages[:7]
elif not st.session_state.progress['level6']:
    pages = pages[:8]
elif not st.session_state.progress['advanced_mantras']:
    pages = pages[:9]
elif not st.session_state.progress['vedic_math']:
    pages = pages[:10]
elif not st.session_state.progress['yoga_sutras']:
    pages = pages[:11]
elif not st.session_state.progress['bhagavad_gita']:
    pages = pages[:12]
elif not st.session_state.progress['maheshwara_sutras']:
    pages = pages[:13]
else:
    pages = pages[:]

page = st.sidebar.selectbox("Choose your adventure", pages)

if page == "Home":
    st.header("What is Śabdāstra?")
    st.write("""
    Śabdāstra means “Word-Weapon,” but it's about creating and protecting with words! 
    It's like coding + mantras + emotions. Words have power: sounds (like 'ka' for sharp), rules (grammar), and feelings (Bhāva like courage 🦁).
    Complete quests to earn XP and unlock levels! Start with Sanskrit Phonetics or Level 1.
    New: Dive into Advanced Mantras, Vedic Math, Yoga Sutras, Bhagavad Gita, Maheshwara Sutras, and Panini Grammar for master-level powers! Mantras boost quests like Chakra and Shield.
    """)

elif page == "Sanskrit Phonetics":
    st.header("Explore Sanskrit Phonetics 🕉️")
    st.write("""
    Sanskrit sounds are the foundation of Śabdāstra! Each phonetic has a unique power and place of pronunciation.
    Learn vowels and consonants, then test your knowledge in interactive quizzes. Now accounts for all Sanskrit phonemes!
    Use phonetic_read('sound') with Roman transliterations like 'a', 'aa', 'k', 'kh', etc.
    """)
    
    # Interactive content
    st.subheader("Vowels (Svara)")
    st.write("Examples: a (short), aa (long ā), i, ii (ī), etc.")
    code_input_v = st.text_area("Read a vowel phonetic:", "phonetic_read('a')")
    if st.button("Read Vowel!"):
        result = interpret_sabdāstra(code_input_v)
        st.write(result)
    
    st.subheader("Consonants (Vyanjana)")
    st.write("Examples: k (ka), kh (kha), g (ga), etc.")
    code_input_c = st.text_area("Read a consonant phonetic:", "phonetic_read('k')")
    if st.button("Read Consonant!"):
        result = interpret_sabdāstra(code_input_c)
        st.write(result)
    
    st.subheader("Additional Sounds")
    st.write("Anusvara: am (aṃ), Visarga: ah (aḥ)")
    code_input_a = st.text_area("Read additional sound:", "phonetic_read('am')")
    if st.button("Read Additional!"):
        result = interpret_sabdāstra(code_input_a)
        st.write(result)
    
    # Expanded Interactive Quiz
    st.subheader("Phonetics Quiz Time! 📝")
    questions = [
        {"q": "What does 'a' represent?", "options": ["Creation", "Sharp", "Flow"], "ans": "Creation"},
        {"q": "Where is 'ka' pronounced?", "options": [" Lips", "Throat", "Tongue"], "ans": "Throat"},
        {"q": "Which sound is nurturing?", "options": ["ka", "sa", "ma"], "ans": "ma"},
        {"q": "What is 'aa'?", "options": ["Short a", "Long ā", "Diphthong"], "ans": "Long ā"},
        {"q": "Which is a retroflex sound?", "options": ["t", "ṭ", "c"], "ans": "ṭ"},
        {"q": "What is anusvara?", "options": ["Nasal vowel", "Aspirate", "Sibilant"], "ans": "Nasal vowel"}
    ]
    random.shuffle(questions)
    score = 0
    for i, q in enumerate(questions):
        ans = st.radio(q["q"], q["options"], key=f"quiz_phon{i}")
        if ans == q["ans"]:
            score += 1
    if st.button("Submit Quiz"):
        st.write(f"You scored {score}/{len(questions)}!")
        if score >= 5:
            award_xp('quest9')
            st.session_state.sanskrit_phonetics = True
            st.success("Phonetics mastered! Unlock Level 1.")

elif page == "Level 1: Basics":
    st.header("Level 1: Beginner Zone 🌱")
    st.write("""
    Unlock: Sound Reader, Code Speaker, Bhāva Infusion.
    Learn that sounds matter, how to speak commands, and add feelings!
    Complete quests for XP.
    """)
    
    st.subheader("Quest: Sound Explorer")
    st.write(st.session_state.quests['quest1']['desc'])
    quiz1_options = ["Nurturing", "Sharp energy", "Peace"]
    quiz1 = st.radio("What does 'ka' represent?", quiz1_options, key="q1")
    if st.button("Check Answer"):
        if quiz1 == "Sharp energy":
            st.success("Correct! +10 Focus Buff unlocked.")
            award_xp('quest1')
        else:
            st.error("Try again!")
    
    st.subheader("Quest: Command Caster")
    st.write(st.session_state.quests['quest2']['desc'])
    code_input = st.text_area("Try a command:", "vakya('hello')", key="code1")
    if st.button("Cast Spell!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
        if "executed" in result:
            award_xp('quest2')
    
    st.subheader("Quest: Bhāva Weaver")
    st.write(st.session_state.quests['quest3']['desc'])
    bhava_select = st.selectbox("Choose Bhāva:", ["courage", "peace"], key="bhava1")
    code_input2 = st.text_area("Infuse your command:", f"vakya('shield', bhava='{bhava_select}')", key="code2")
    if st.button("Infuse!"):
        result = interpret_sabdāstra(code_input2)
        st.write(result)
        if "Infused" in result:
            award_xp('quest3')

elif page == "Level 2: Core":
    st.header("Level 2: Apprentice Zone 🔥")
    st.write("Unlock: Grammar Forge, Pattern Casting.")
    
    st.subheader("Quest: Grammar Guardian")
    st.write(st.session_state.quests['quest4']['desc'])
    code_input = st.text_area("Forge a command:", "grammar_forge('subject verb object')", key="code3")
    if st.button("Forge!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
        if "forged" in result:
            award_xp('quest4')
    
    st.subheader("Quest: Pattern Pro")
    st.write(st.session_state.quests['quest5']['desc'])
    pattern_type = st.slider("Pattern complexity (1-5):", 1, 5, key="pattern1")
    code_input2 = st.text_area("Cast a pattern:", f"pattern_cast('repeat hello {pattern_type} times')", key="code4")
    if st.button("Cast!"):
        result = interpret_sabdāstra(code_input2)
        st.write(result)
        if pattern_type > 3:
            award_xp('quest5')
        else:
            st.info("Increase complexity for full XP!")

elif page == "Level 3: Systems":
    st.header("Level 3: Adept Zone 🌀")
    st.write("Unlock: Chakra Channeling. Integrate mantras for enhanced channeling!")
    
    st.subheader("Quest: Chakra Connector")
    st.write(st.session_state.quests['quest6']['desc'])
    chakra_select = st.multiselect("Select chakras:", ["root", "heart", "mind"], key="chakra1")
    mantra_select = st.selectbox("Choose a mantra to enhance channeling:", ["gayatri", "om namah shivaya", "om mani padme hum"], key="mantra_chakra")
    code_input = st.text_area("Channel a chakra with mantra:", f"chakra_channel('{chakra_select[0] if chakra_select else 'heart'}')  # Add mantra_chant('{mantra_select}') for boost", key="code5")
    if st.button("Channel!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
        if len(chakra_select) >= 2 and "mantra_chant" in code_input:
            award_xp('quest6')
        elif "mantra_chant" not in code_input:
            st.info("Incorporate a mantra chant for full quest completion!")

elif page == "Level 4: Defense":
    st.header("Level 4: Guardian Zone 🛡️")
    st.write("Unlock: Mantra Shield, Hash Seal. Use protective mantras to strengthen shields!")
    
    st.subheader("Quest: Shield Master")
    st.write(st.session_state.quests['quest7']['desc'])
    mantra_select = st.selectbox("Choose a protective mantra:", ["mahamrityunjaya", "om namah shivaya"], key="mantra_shield")
    code_input = st.text_area("Activate shield with mantra:", f"mantra_shield('{mantra_select}')", key="code6")
    if st.button("Shield Up!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
        if mantra_select in result:
            award_xp('quest7')
        else:
            st.info("Use a mantra in the shield command for full XP!")
    
    code_input2 = st.text_area("Seal it:", "hash_seal('secret')", key="code7")
    if st.button("Seal!"):
        result = interpret_sabdāstra(code_input2)
        st.write(result)

elif page == "Level 5: Paths":
    st.header("Level 5: Advanced Paths 🌌")
    st.write("Choose your specialization!")
    
    path = st.selectbox("Pick a path:", ["Architect of Logic", "Keeper of Bhāva", "Seer of Systems"], key="path1")
    
    if path == "Architect of Logic":
        st.write("Build systems! Ultimate: shastra_core()")
        code_input = st.text_area("Build core:", "shastra_core()", key="code8")
        if st.button("Build!"):
            result = interpret_sabdāstra(code_input)
            st.write(result)
    elif path == "Keeper of Bhāva":
        st.write("Harmonize emotions! Ultimate: rasa_harmony()")
        code_input = st.text_area("Harmonize:", "rasa_harmony()", key="code9")
        if st.button("Harmonize!"):
            result = interpret_sabdāstra(code_input)
            st.write(result)
    elif path == "Seer of Systems":
        st.write("Predict futures! Ultimate: kaala_map()")
        code_input = st.text_area("Map time:", "kaala_map()", key="code10")
        if st.button("Map!"):
            result = interpret_sabdāstra(code_input)
            st.write(result)
    
    if st.button("Commit to Path"):
        st.session_state.progress['level5'] = path
        award_xp('quest8')
        st.success(f"Path chosen: {path}! Unlock Mastery.")

elif page == "Level 6: Mastery":
    st.header("Level 6: Legendary Tier 👑")
    st.write("You've become a Śabdāstra Master! 🦚")
    st.write("Fuse all skills. Words shape reality ethically.")
    st.success("Congratulations, Dharma Coder! You've defeated Chaos with Truth, Order, and Compassion.")
    st.balloons()

elif page == "Advanced Mantras":
    st.header("Advanced Sanskrit Mantras 🕉️✨")
    st.write("""
    Unlock the power of ancient Sanskrit mantras! These are advanced 'word-weapons' for protection, wisdom, and healing.
    Chant them in Śabdāstra code to see their meanings and benefits. Complete the quest to earn XP!
    Examples: Gayatri (wisdom), Mahamrityunjaya (healing), Om Namah Shivaya (balance).
    """)
    
    st.subheader("Quest: Mantra Mystic")
    st.write(st.session_state.quests['quest10']['desc'])
    mantra_select = st.selectbox("Choose a mantra to chant:", ["gayatri", "mahamrityunjaya", "om namah shivaya", "aing namah", "om mani padme hum"], key="mantra1")
    code_input = st.text_area("Chant the mantra:", f"mantra_chant('{mantra_select}')", key="code11")
    if st.button("Chant!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
        # Interactive element: Quiz on mantra benefits
        quiz_mantra = st.radio(f"What is the benefit of '{mantra_select}'?", ["Healing", "Wisdom", "Compassion"], key="quiz_mantra")
        if st.button("Check Mantra Knowledge"):
            correct_answers = {
                "gayatri": "Wisdom",
                "mahamrityunjaya": "Healing",
                "om namah shivaya": "Healing",  # Balance, but close to healing
                "aing namah": "Wisdom",
                "om mani padme hum": "Compassion"
            }
            if quiz_mantra == correct_answers.get(mantra_select):
                st.success("Correct! Mantra power unlocked.")
                award_xp('quest10')
            else:
                st.error("Try again! Hint: Check the chant result.")

elif page == "Vedic Mathematics":
    st.header("Explore Vedic Mathematics 🔢🕉️")
    st.write("""
    Vedic Math is ancient Indian techniques for fast calculations! Learn tricks for multiplication, squaring, and more based on 16 sutras and 13 sub-sutras.
    Use Śabdāstra code to practice. Great for kids to solve math quickly and accurately.
    """)
    
    st.subheader("Quest: Vedic Math Wizard")
    st.write(st.session_state.quests['quest11']['desc'])
    
    st.subheader("The 16 Vedic Sutras")
    vedic_sutras = [
        "1. Ekādhikena Pūrvena: By one more than the previous one. Used for squaring numbers ending in 5, multiplying by 11.",
        "2. Nikhilam Navataścaramam Daśataḥ: All from 9 and the last from 10. For multiplication near bases like 10, 100.",
        "3. Ūrdhva-Tiryagbhyām: Vertically and crosswise. General multiplication and division.",
        "4. Parāvartya Yojayet: Transpose and adjust. For division when divisor is close to base.",
        "5. Śūnyam Sāmyasamuccaye: When the sum is the same then the sum is zero. For equations.",
        "6. Anurūpyeṇa: Proportionately. For multiplication with working base.",
        "7. Saṅkalana-vyavakalanābhyām: By addition and by subtraction. For solving equations.",
        "8. Pūraṇāpūraṇābhyām: By the completion or non-completion. For fractions.",
        "9. Calana-Kalanābhyām: Differential calculus. For calculus applications.",
        "10. Yāvadūnam: Whatever the extent of its deficiency. For squaring numbers close to base.",
        "11. Vyastisamansti: Specific and general. For division.",
        "12. Śeṣāṇyāṅkena Carameṇa: The remainders by the last digit. For divisibility.",
        "13. Sopantyadvayamantyam: The ultimate and twice the penultimate. For divisibility by 11.",
        "14. Ekanyūnena Pūrvena: By one less than the previous one. For multiplication by 9, 99.",
        "15. Guṇitasamuccayaḥ: The product of the sum is equal to the sum of the product. For verification.",
        "16. Guṇakasamuccayaḥ: The factors of the sum is equal to the sum of the factors. For factorization."
    ]
    for sutra in vedic_sutras:
        st.write(sutra)
    
    # Existing Vedic tools plus new
    st.subheader("Vedic Division (Parāvartya)")
    dividend = st.number_input("Dividend:", min_value=1)
    divisor = st.number_input("Divisor:", min_value=1)
    code_div = st.text_area("Divide:", f"vedic_divide({dividend}, {divisor})")
    if st.button("Divide!"):
        result = interpret_sabdāstra(code_div)
        st.write(result)
    
    st.subheader("Vedic Cubing (Anurūpyeṇa)")
    num_cube = st.number_input("Number to cube:", min_value=1)
    code_cube = st.text_area("Cube:", f"vedic_cube({num_cube})")
    if st.button("Cube It!"):
        result = interpret_sabdāstra(code_cube)
        st.write(result)
    
    # ... (add more tools if needed)
    
    if st.button("Complete Vedic Quests"):
        award_xp('quest11')
        st.success("Vedic tricks mastered!")

elif page == "Yoga Sutras":
    st.header("Explore Yoga Sutras 🧘‍♂️🕉️")
    st.write("""
    The Yoga Sutras of Patanjali are ancient aphorisms on the practice and philosophy of yoga. Explore key sutras, their translations, and explanations.
    Use Śabdāstra code like sutra_read('1.2') to delve into wisdom. Complete the quest with a quiz!
    """)
    
    st.subheader("Quest: Sutra Scholar")
    st.write(st.session_state.quests['quest12']['desc'])
    
    st.subheader("Read a Sutra")
    sutra_num = st.selectbox("Choose a sutra number:", sorted(list(set(["1.1", "1.2", "1.3", "1.4", "1.5", "1.13", "1.14", "1.27", "1.34", "2.1", "2.3", "2.15", "2.28", "2.29", "2.30", "2.31", "2.32", "2.46", "2.49", "2.54", "3.1", "3.2", "3.3", "3.49", "4.1", "4.15", "4.31", "4.34"]))), key="sutra_select")
    code_input = st.text_area("Read the sutra:", f"sutra_read('{sutra_num}')", key="code14")
    if st.button("Interpret Sutra!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
    
    # More interactive Quiz
    st.subheader("Sutra Quiz Time! 📝")
    st.write("Answer multiple quizzes to test your knowledge!")
    questions = [
        {"q": "What does Sutra 1.2 define yoga as?", "options": ["Control of the body", "Control of the mind", "Control of breath"], "ans": "Control of the mind"},
        {"q": "Sutra 2.46 emphasizes what in asana?", "options": ["Flexibility", "Steadiness and ease", "Strength"], "ans": "Steadiness and ease"},
        {"q": "What is Samadhi in Sutra 3.3?", "options": ["Deep concentration", "Breath control", "Posture"], "ans": "Deep concentration"},
        {"q": "Sutra 1.3 describes what state?", "options": ["Mind fluctuations", "Seer in own nature", "Practice effort"], "ans": "Seer in own nature"},
        {"q": "What are the five kleshas in 2.3?", "options": ["Yamas", "Afflictions like ignorance", "Limbs of yoga"], "ans": "Afflictions like ignorance"},
        {"q": "Sutra 4.34 defines what?", "options": ["Kaivalya", "Samadhi", "Pranayama"], "ans": "Kaivalya"}
    ]
    random.shuffle(questions)
    with st.form(key="sutra_quiz_form"):
        responses = {}
        for i, q in enumerate(questions):
            responses[i] = st.radio(q["q"], q["options"], key=f"quiz_sutra{i}")
        submit = st.form_submit_button("Submit Sutra Quiz")
    if submit:
        score = sum(1 for i, q in enumerate(questions) if responses[i] == q["ans"])
        st.write(f"You scored {score}/{len(questions)}!")
        if score >= len(questions) - 1:  # High score threshold
            award_xp('quest12')
            st.success("Sutras mastered! Infinite wisdom unlocked.")
        else:
            st.info("Study more sutras and try again!")

elif page == "Bhagavad Gita":
    st.header("Explore Bhagavad Gita 📖🕉️")
    st.write("""
    The Bhagavad Gita is a sacred dialogue between Lord Krishna and Arjuna on duty, righteousness, and devotion.
    Explore key verses, their translations, and explanations. Use Śabdāstra code like gita_read('2.47') to learn timeless wisdom.
    Complete the quest with a quiz!
    """)
    
    st.subheader("Quest: Gita Guide")
    st.write(st.session_state.quests['quest13']['desc'])
    
    st.subheader("Read a Gita Verse")
    gita_num = st.selectbox("Choose a verse number:", sorted(list(set(["1.1", "2.14", "2.20", "2.47", "3.21", "4.7", "4.11", "5.21", "6.5", "9.26", "9.34", "12.5", "18.65", "18.66"]))), key="gita_select")
    code_input = st.text_area("Read the verse:", f"gita_read('{gita_num}')", key="code15")
    if st.button("Interpret Verse!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
    
    # Interactive Quiz for Gita
    st.subheader("Gita Quiz Time! 📝")
    questions = [
        {"q": "What does 2.47 teach?", "options": ["Attachment to results", "Right to action only", "Avoid work"], "ans": "Right to action only"},
        {"q": "In 4.7, when does Krishna descend?", "options": ["Decline in dharma", "Every day", "Never"], "ans": "Decline in dharma"},
        {"q": "What is promised in 18.66?", "options": ["Surrender liberates", "Fight always", "Wealth"], "ans": "Surrender liberates"},
        {"q": "Verse 6.5 says mind is?", "options": ["Always enemy", "Friend or enemy", "Irrelevant"], "ans": "Friend or enemy"}
    ]
    random.shuffle(questions)
    with st.form(key="gita_quiz_form"):
        responses = {}
        for i, q in enumerate(questions):
            responses[i] = st.radio(q["q"], q["options"], key=f"quiz_gita{i}")
        submit = st.form_submit_button("Submit Gita Quiz")
    if submit:
        score = sum(1 for i, q in enumerate(questions) if responses[i] == q["ans"])
        st.write(f"You scored {score}/{len(questions)}!")
        if score == len(questions):
            award_xp('quest13')
            st.success("Gita verses mastered! Dharma unlocked.")

elif page == "Maheshwara Sutras":
    st.header("Explore Maheshwara Sutras (Shiva Sutras) 🕉️🛡️")
    st.write("""
    The Maheshwara Sutras are 14 aphorisms revealed to Panini by Lord Shiva, listing Sanskrit phonemes in a compact form for grammar.
    They form the basis of pratyāhāras in Sanskrit linguistics. Explore the sutras and their phonemes.
    Use phonetic_read for individual sounds.
    """)
    
    st.subheader("Quest: Maheshwara Master")
    st.write(st.session_state.quests['quest14']['desc'])
    
    # List of Maheshwara Sutras
    maheshwara_sutras = [
        "1. a i u ṇ - Vowels: a, i, u",
        "2. ṛ ḷ k - Vowels: ṛ, ḷ",
        "3. e o ṅ - Vowels: e, o",
        "4. ai au c - Vowels: ai, au",
        "5. ha ya va ra ṭ - Semivowels: ha, ya, va, ra",
        "6. la ṇ - Semivowel: la",
        "7. ña ma ṅa ṇa na m - Nasals: ña, ma, ṅa, ṇa, na",
        "8. jha bha ñ - Voiced aspirates: jha, bha",
        "9. gha ḍha dha ṣ - Voiced aspirates: gha, ḍha, dha",
        "10. ja ba ga ḍa da ś - Voiced stops: ja, ba, ga, ḍa, da",
        "11. kha pha cha ṭha tha ca ṭa ta v - Voiceless aspirates and stops: kha, pha, cha, ṭha, tha, ca, ṭa, ta",
        "12. ka pa y - Voiceless stops: ka, pa",
        "13. śa ṣa sa r - Sibilants: śa, ṣa, sa",
        "14. ha l - Aspirate: ha"
    ]
    st.subheader("The 14 Maheshwara Sutras")
    for sutra in maheshwara_sutras:
        st.write(sutra)
    
    # Interactive: Read a phoneme from sutras
    st.subheader("Explore Phonemes from Sutras")
    sound_select = st.selectbox("Choose a sound:", ["a", "i", "u", "r", "rr", "l", "ll", "e", "o", "ai", "au", "ha", "ya", "va", "ra", "la", "nya", "ma", "nga", "na", "na", "jha", "bha", "gha", "dha", "dha", "ja", "ba", "ga", "da", "da", "kha", "pha", "cha", "tha", "tha", "ca", "ta", "ta", "ka", "pa", "sha", "ssa", "sa", "ha"])
    code_input = st.text_area("Read phonetic:", f"phonetic_read('{sound_select}')")
    if st.button("Read Phoneme!"):
        result = interpret_sabdāstra(code_input)
        st.write(result)
    
    # Quiz for Maheshwara Sutras
    st.subheader("Maheshwara Quiz Time! 📝")
    questions = [
        {"q": "How many Maheshwara Sutras are there?", "options": ["10", "14", "20"], "ans": "14"},
        {"q": "What does the first sutra list?", "options": ["Consonants", "Vowels a i u", "Sibilants"], "ans": "Vowels a i u"},
        {"q": "Which sutra includes sibilants śa ṣa sa?", "options": ["13", "14", "11"], "ans": "13"},
        {"q": "The sutras were revealed to whom?", "options": ["Vyasa", "Panini", "Valmiki"], "ans": "Panini"}
    ]
    random.shuffle(questions)
    score = 0
    for i, q in enumerate(questions):
        ans = st.radio(q["q"], q["options"], key=f"quiz_mahesh{i}")
        if ans == q["ans"]:
            score += 1
    if st.button("Submit Maheshwara Quiz"):
        st.write(f"You scored {score}/{len(questions)}!")
        if score == len(questions):
            award_xp('quest14')
            st.success("Maheshwara Sutras mastered! Phonemic power unlocked.")

elif page == "Panini Grammar":
    st.header("Explore Panini's Grammar 🕉️📜")
    st.write("""
    Panini's Ashtadhyayi is the foundational text of Sanskrit grammar, with 3,959 sutras organized in 8 chapters.
    Key concepts include sutras (rules), anuvritti (rule inheritance), adhikara (heading rules), pratyaharas (abbreviations for phoneme groups), sandhi (euphonic combination), samasa (compounds), karaka (case relations), and more.
    It uses meta-rules for precision and brevity, influencing modern linguistics and computing.
    Patanjali's Mahabhashya is a great commentary on the Ashtadhyayi, defending Panini against Katyayana, exploring philosophy of language, and providing examples. It references historical events like Yavana attacks on Saketa, dating to 2nd century BCE. The Mahabhashya is essential for understanding Panini's rules in depth, with discussions on sphota theory (burst of meaning) and varna (sound units).
    Katyayana's Varttikas are critical commentaries on Panini's sutras, pointing out omissions, ambiguities, or needs for modification. There are about 4,300 varttikas, addressing loose ends in Ashtadhyayi. Patanjali's Mahabhashya discusses these varttikas, accepting some and rejecting others. Katyayana's work is key in the trimuni tradition (Panini, Katyayana, Patanjali).
    Mahabhashya commentaries include discussions on word-meaning relations (permanent vs. transient), sphota as holistic sound-meaning unit, critiques of Mimamsa and Nyaya schools, and linguistic philosophy. It uses dialogues (vada) to argue points, e.g., whether words are eternal (nitya) or created (karya). Patanjali also comments on social aspects, like language use in different regions.
    Katyayana's Varttikas examples: For sutra 1.1.56, varttika suggests addition for clarity. Many varttikas are on sandhi and verb formations, ensuring the system is complete. Patanjali's responses in Mahabhashya often incorporate them into the tradition.
    """)
    
    st.subheader("Quest: Panini Grammarian")
    st.write(st.session_state.quests['quest15']['desc'])
    
    st.subheader("Key Concepts")
    panini_concepts = [
        "Sutras: Concise rules, e.g., 'iko yaṇaci' for sandhi.",
        "Anuvritti: Carrying forward words from previous sutras for brevity.",
        "Adhikara: Domain-specifying rules that apply to subsequent sutras.",
        "Pratyaharas: Abbreviations like 'ac' for all vowels, from Maheshwara Sutras.",
        "Sandhi: Joining words, e.g., 'deva + iśa = deveśa'.",
        "Samasa: Compounds, e.g., tatpurusha, bahuvrihi.",
        "Karaka: Semantic roles like karta (agent), karma (object).",
        "Dhatu: Verb roots with classes (ganas).",
        "Vibhakti: Case endings for nouns.",
        "Lakara: Verb moods and tenses, like lat (present)."
    ]
    for concept in panini_concepts:
        st.write(concept)
    
    st.subheader("Panini Sutra Examples")
    panini_sutras = [
        "1.1.1: vṛddhir ādaic - Defines vṛddhi vowels: ā, ai, au.",
        "1.4.14: sup-tiṅantaṃ padam - A word ends with nominal or verbal suffix.",
        "3.1.91: dhātoḥ - After a root (for verb formation).",
        "6.1.77: iko yaṇaci - i,u,ṛ,ḷ become y,v,r,l before dissimilar vowels (sandhi).",
        "6.1.87: ād guṇaḥ - a + i/u = e/o (guṇa sandhi).",
        "6.1.101: akaḥ savarṇe dīrghaḥ - Same vowels combine to long vowel.",
        "8.3.23: mo 'nusvāraḥ - m before consonant becomes anusvāra.",
        "3.2.123: vartamāne laṭ - Present tense uses laṭ endings.",
        "2.3.2: karmaṇi dvitīyā - Accusative for object.",
        "4.1.2: svaujasamauṭchṣṭa... - Nominal endings list.",
        "1.3.2: upadeśe 'janunāsika it - Defines it markers as nasal in teaching.",
        "1.1.5: kṅiti ca - Guṇa and vṛddhi don't occur before k, ṅ, it.",
        "8.2.66: sasajuso ruḥ - Final s becomes ruḥ before vowels or soft consonants.",
        "6.1.109: eṅaḥ padāntād ati - e/ o + a = a (lop of e/o).",
        "3.1.68: kartari śap - Śap suffix for present tense active voice.",
        "1.1.49: ṣaṣṭhī stheyasya - Genitive denotes relation.",
        "1.3.3: halantyam - Consonants at end are it markers.",
        "2.4.58: ghu pratyaye - ghu for short vowels before certain suffixes.",
        "3.1.32: sanādyantā dhātavaḥ - Roots with san etc. are derived roots.",
        "4.1.76: taddhitāḥ - Secondary derivatives (taddhita suffixes)."
    ]
    for sutra in panini_sutras:
        st.write(sutra)
    
    st.subheader("Sanskrit Sandhi Rules")
    st.write("""
    Sandhi is euphonic combination of sounds at word junctions. Types:
    - Vowel Sandhi: a + i = e (guṇa), a + a = ā (dirgha), i + u = yu (yan).
    - Visarga Sandhi: aḥ + a = o ' (lop with o), aḥ + c = aś c.
    - Consonant Sandhi: t + c = cc (doubling), n + t = nt (no change), m + consonant = anusvāra.
    Examples:
    - deva + indra = devendra (a + i = e).
    - rāmaḥ + asti = rāmo 'sti (ḥ + a = o ').
    - jagat + nātha = jagannātha (t + n = nn).
    Sandhi ensures smooth pronunciation and is governed by Panini sutras like 6.1.77.
    """)
    
    # Interactive Quiz
    st.subheader("Panini Quiz Time! 📝")
    questions = [
        {"q": "What is Ashtadhyayi?", "options": ["8 chapters", "16 sutras", "Vedic math"], "ans": "8 chapters"},
        {"q": "Pratyaharas are?", "options": ["Phoneme abbreviations", "Verb roots", "Compounds"], "ans": "Phoneme abbreviations"},
        {"q": "Sandhi means?", "options": ["Joining words", "Separation", "Nouns"], "ans": "Joining words"},
        {"q": "Karaka refers to?", "options": ["Semantic roles", "Tenses", "Adjectives"], "ans": "Semantic roles"},
        {"q": "Sutra 6.1.77 is for?", "options": ["Vowel sandhi", "Verb endings", "Compounds"], "ans": "Vowel sandhi"},
        {"q": "Example of dirgha sandhi?", "options": ["a + a = ā", "a + i = e", "m + c = ṃ"], "ans": "a + a = ā"}
    ]
    random.shuffle(questions)
    score = 0
    for i, q in enumerate(questions):
        ans = st.radio(q["q"], q["options"], key=f"quiz_panini{i}")
        if ans == q["ans"]:
            score += 1
    if st.button("Submit Panini Quiz"):
        st.write(f"You scored {score}/{len(questions)}!")
        if score >= 5:
            award_xp('quest15')
            st.success("Panini grammar mastered! Linguistic power unlocked.")
