from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    INBOUND = 'Inbound'
    OUTBOUND = 'Outbound'
    CAMPAIGN_TYPE_CHOICES = [
        (INBOUND, 'Inbound'),
        (OUTBOUND, 'Outbound'),
    ]

    RUNNING = 'Running'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (RUNNING, 'Running'),
        (PAUSED, 'Paused'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=CAMPAIGN_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=RUNNING)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='campaigns')

    def __str__(self):
        return self.name

class CampaignResult(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    cost = models.FloatField()
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField()
    recording_url = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='results')

    def __str__(self):
        return self.name
