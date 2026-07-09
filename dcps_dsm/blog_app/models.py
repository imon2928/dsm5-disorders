from django.db import models

class BlogModel(models.Model):
    # ক্যাটাগরি সেক্টর চয়েস
    CATEGORY_CHOICES = [
        
        ('psychological-content', 'Psychological Content'),
        ('intellectual-disabilities', 'Intellectual Disabilities'),
        ('communication-disorders', 'Communication Disorders'),
        ('autism-spectrum', 'Autism Spectrum Disorder'),
        ('adhd', 'Attention Deficit Hyperactivity Disorder (ADHD)'),
        ('specific-learning', 'Specific Learning Disability'),
        ('motor-disorders','Motor Disorders'),
        ('schizophrenia-spectrum','Schizophrenia Spectrum Disorder'),
        ('bipolar-disorders','Bipolar Disorders'),
        ('depressive-disorders','Depressive Disorders'),
        ('anxiety-disorders','Anxiety Disorders'),
        ('ocd','Obsessive-Compulsive Disorder'),
        ('trauma-disorders','Trauma and Stressor-Related Disorders'),
        ('dissociative-disorders','Dissociative Disorders'),
        ('somatic-disorders','Somatic Symptom Disorders'),
        ('eating-disorders','Eating Disorders'),
        ('sleep-disorders','Sleep Disorders'),
        ('personality-disorders','Personality Disorders'),
        ('neurocognitive-disorders','Neurocognitive Disorders'),
        # তোমার বাকি ক্যাটাগরিগুলোর 'id' এখানে এভাবে যোগ করতে পারো...
    ]

    # কন্টেন্ট টাইপ সেক্টর চয়েস
    TYPE_CHOICES = [
        ('neuro', 'Neurological Causes'),
        ('psychological', 'Psychological Causes'),
        ('dsm5', 'DSM-5 Diagnosis Criteria'),
    ]

    title = models.CharField(max_length=400)
    content = models.TextField()
    author = models.CharField(max_length=300)
    
    # নতুন ৩টি ফিল্ড যা সেক্টর আলাদা করবে
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='anxiety-disorders')
    disorder_slug = models.CharField(max_length=100, help_text="intellectual-disability,global-developmental-delay, unspecified-intellectual-disability, language-disorder, speech-sound-disorder, childhood-onset-fluency, social-communication, unspecified-communication, asd-level1, asd-level2, asd-level3, adhd-inattentive, adhd-hyperactive, adhd-combined, adhd-other, dyslexia, dysgraphia, dyscalculia, developmental-coordination, stereotypic-movement, schizophrenia, schizoaffective, delusional, bipolar-i, bipolar-ii, cyclothymic, disruptive-mood-dysregulation, major-depressive, persistent-depressive, premenstrual-dysphoric, separation-anxiety, selective-mutism, specific-phobia, social-anxiety, panic-disorder, agoraphobia, generalized-anxiety, substance-medication-induced-anxiety, ocd-hoarding-type, ocd-contamination-type, ocd-symmetry-type, ocd-intrusive-thoughts-type, ptsd-acute-stress-disorder-type, ptsd-complex-type, ptsd-childhood-type, dissociative-identity-disorder-type, dissociative-amnesia-type, depersonalization-derealization-type, somatic-symptom-disorder-type, illness-anxiety-disorder-type, conversion-disorder-type, factitious-disorder-type, anorexia-nervosa-restricting-type, anorexia-nervosa-binge-eating-purging-type, bulimia-nervosa-purging-type, bulimia-nervosa-non-purging-type, tourettes, persistent-tic, provisional-tic, schizotypal-pd, delusional-disorder, brief-psychotic, schizophreniform, schizophrenia, schizoaffective, bipolar-1, bipolar-2,cyclothymic, substance-induced-bipolar, dmdd, major-depression, persistent-depressive, pmdd, substance-induced-depressive, separation-anxiety, selective-mutism, specific-phobia, social-anxiety, panic-disorder, agoraphobia, gad, ocd, body-dysmorphic, hoarding, trichotillomania, excoriation, reactive-attachment, disinhibited-social, ptsd, acute-stress, adjustment-disorders, did, dissociative-amnesia, depersonalization, somatic-symptom, illness-anxiety, conversion-disorder, factitious-disorder, pica, rumination, arfid, anorexia-nervosa, bulimia-nervosa, binge-eating, insomnia, hypersomnolence, narcolepsy, circadian-rhythm, nightmare-disorder, rem-sleep, restless-legs, paranoid-pd, schizoid-pd, antisocial-pd, histrionic-pd, narcissistic-pd, avoidant-pd, dependent-pd, ocpd, delirium, alzheimers-ncd, vascular-ncd, lewy-body-ncd, frontotemporal-ncd, tbi-ncd, parkinsons-ncd, classical-conditioning, operant-conditioning, cognitive-dissonance, defense-mechanisms,maslow-hierarchy")
    content_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='neuro')

    def __str__(self):
        return f"{self.title} ({self.disorder_slug} - {self.content_type})"