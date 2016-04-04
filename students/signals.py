# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student, Group, Exam


@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name,
            student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name,
            student.last_name, student.id)

@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name,
        student.last_name, student.id)


@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    if kwargs['created']:
        logger.info("Group added: %s %s (ID: %d)", group.title,
        group.leader, group.id)
    else:
        logger.info("Group updated: %s %s (ID: %d)", group.title,
        group.leader, group.id)

@receiver(post_delete, sender=Group)
def log_group_deleted_event(sender, **kwargs):
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    logger.info("Group deleted: %s (ID: %d)", group.title,
    group.id)


@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    if kwargs['created']:
        logger.info("Exam added: %s %s %s %s (ID: %d)", exam.subject,
        exam.date, exam.teacher, exam.group, exam.id)
    else:
        logger.info("Exam updated: %s %s %s %s (ID: %d)", exam.subject,
        exam.date, exam.teacher, exam.group, exam.id)

@receiver(post_delete, sender=Exam)
def log_exam_deleted_event(sender, **kwargs):
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    logger.info("Exam deleted: %s %s %s %s (ID: %d)", exam.subject,
    exam.date, exam.teacher, exam.group, exam.id)
