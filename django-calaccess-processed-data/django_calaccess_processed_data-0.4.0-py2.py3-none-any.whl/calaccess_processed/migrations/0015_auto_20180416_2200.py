# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-16 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '__first__'),
        ('calaccess_processed', '0014_pgcrypto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FilerIDValue',
        ),
        migrations.DeleteModel(
            name='FilingIDValue',
        ),
        migrations.AlterUniqueTogether(
            name='form460filingversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460filingversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460filingversion',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleaitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleaitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleaitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleaitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleaitemversion',
            name='filing_version',
        ),
        migrations.RemoveField(
            model_name='form460scheduleasummary',
            name='filing',
        ),
        migrations.RemoveField(
            model_name='form460scheduleasummaryversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleb1item',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleb1item',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleb1itemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleb1itemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleb1itemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleb2item',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleb2item',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleb2itemold',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleb2itemold',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleb2itemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleb2itemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleb2itemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleb2itemversionold',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleb2itemversionold',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleb2itemversionold',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulecitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulecitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulecitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460schedulecitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulecitemversion',
            name='filing_version',
        ),
        migrations.RemoveField(
            model_name='form460schedulecsummary',
            name='filing',
        ),
        migrations.RemoveField(
            model_name='form460schedulecsummaryversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleditem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleditem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleditemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleditemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleditemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleeitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleeitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleeitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleeitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleeitemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleesubitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleesubitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleesubitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleesubitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleesubitemversion',
            name='filing_version',
        ),
        migrations.RemoveField(
            model_name='form460scheduleesummary',
            name='filing',
        ),
        migrations.RemoveField(
            model_name='form460scheduleesummaryversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulefitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulefitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulefitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460schedulefitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulefitemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulegitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulegitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulegitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460schedulegitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulegitemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleh2itemold',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleh2itemold',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleh2itemversionold',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleh2itemversionold',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleh2itemversionold',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulehitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulehitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulehitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460schedulehitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460schedulehitemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleiitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleiitem',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form460scheduleiitemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form460scheduleiitemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form460scheduleiitemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form497filingversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form497filingversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form497filingversion',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form497part1item',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form497part1item',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form497part1itemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form497part1itemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form497part1itemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form497part2item',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form497part2item',
            name='filing',
        ),
        migrations.AlterUniqueTogether(
            name='form497part2itemversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form497part2itemversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form497part2itemversion',
            name='filing_version',
        ),
        migrations.AlterUniqueTogether(
            name='form501filingversion',
            unique_together=set([]),
        ),
        migrations.AlterIndexTogether(
            name='form501filingversion',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='form501filingversion',
            name='filing',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestOptionProxy',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDBallotMeasureContestSourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidacyProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidacySourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidateContestPostProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidateContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDCandidateContestSourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDDivisionProxy',
        ),
        migrations.DeleteModel(
            name='OCDElectionIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDElectionProxy',
        ),
        migrations.DeleteModel(
            name='OCDElectionSourceProxy',
        ),
        migrations.DeleteModel(
            name='OCDFlatBallotMeasureContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDFlatCandidacyProxy',
        ),
        migrations.DeleteModel(
            name='OCDFlatRetentionContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDMembershipProxy',
        ),
        migrations.DeleteModel(
            name='OCDOrganizationIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDOrganizationNameProxy',
        ),
        migrations.DeleteModel(
            name='OCDOrganizationProxy',
        ),
        migrations.DeleteModel(
            name='OCDPartyProxy',
        ),
        migrations.DeleteModel(
            name='OCDPersonIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDPersonNameProxy',
        ),
        migrations.DeleteModel(
            name='OCDPersonProxy',
        ),
        migrations.DeleteModel(
            name='OCDPostProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestIdentifierProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestOptionProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestProxy',
        ),
        migrations.DeleteModel(
            name='OCDRetentionContestSourceProxy',
        ),
        migrations.DeleteModel(
            name='RawFilerToFilerTypeCdProxy',
        ),
        migrations.DeleteModel(
            name='ScrapedCandidateElectionProxy',
        ),
        migrations.DeleteModel(
            name='ScrapedCandidateProxy',
        ),
        migrations.DeleteModel(
            name='ScrapedIncumbentElectionProxy',
        ),
        migrations.DeleteModel(
            name='ScrapedIncumbentProxy',
        ),
        migrations.DeleteModel(
            name='ScrapedPropositionElectionProxy',
        ),
        migrations.DeleteModel(
            name='ScrapedPropositionProxy',
        ),
        migrations.DeleteModel(
            name='Form460FilingVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleAItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleAItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleASummary',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleASummaryVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleB1Item',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleB1ItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleB2Item',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleB2ItemOld',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleB2ItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleB2ItemVersionOld',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleCItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleCItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleCSummary',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleCSummaryVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleDItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleDItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleEItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleEItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleESubItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleESubItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleESummary',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleESummaryVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleFItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleFItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleGItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleGItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleH2ItemOld',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleH2ItemVersionOld',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleHItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleHItemVersion',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleIItem',
        ),
        migrations.DeleteModel(
            name='Form460ScheduleIItemVersion',
        ),
        migrations.DeleteModel(
            name='Form497FilingVersion',
        ),
        migrations.DeleteModel(
            name='Form497Part1Item',
        ),
        migrations.DeleteModel(
            name='Form497Part1ItemVersion',
        ),
        migrations.DeleteModel(
            name='Form497Part2Item',
        ),
        migrations.DeleteModel(
            name='Form497Part2ItemVersion',
        ),
        migrations.DeleteModel(
            name='Form501FilingVersion',
        ),
        migrations.DeleteModel(
            name='Form501Filing',
        ),
        migrations.DeleteModel(
            name='Form497Filing',
        ),
        migrations.DeleteModel(
            name='Form460Filing',
        ),
    ]
