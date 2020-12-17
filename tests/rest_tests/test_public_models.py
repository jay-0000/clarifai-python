# -*- coding: utf-8 -*-

import logging
import unittest

from clarifai.rest import ClarifaiApp

from . import sample_inputs


class TestPublicModels(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.app = ClarifaiApp(log_level=logging.WARN)

  def test_predict_with_apparel_model(self):
    res = self.app.public_models.apparel_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_color_mode(self):
    res = self.app.public_models.color_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_face_detection_model(self):
    res = self.app.public_models.face_detection_model.predict_by_url(
        url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_face_embedding_model(self):
    res = self.app.public_models.face_embedding_model.predict_by_url(
        url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_food_model(self):
    res = self.app.public_models.food_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_general_embedding_model(self):
    res = self.app.public_models.general_embedding_model.predict_by_url(
        url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_general_model(self):
    res = self.app.public_models.general_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_landscape_quality_model(self):
    res = self.app.public_models.landscape_quality_model.predict_by_url(
        url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_logo_model(self):
    res = self.app.public_models.logo_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_moderation_model(self):
    res = self.app.public_models.moderation_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_nsfw_model(self):
    res = self.app.public_models.nsfw_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_portrait_model(self):
    res = self.app.public_models.portrait_quality_model.predict_by_url(
        url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_textures_and_patterns_model(self):
    res = self.app.public_models.textures_and_patterns_model.predict_by_url(
        url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_travel_model(self):
    res = self.app.public_models.travel_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])

  def test_predict_with_wedding_model(self):
    res = self.app.public_models.wedding_model.predict_by_url(url=sample_inputs.METRO_IMAGE_URL)
    self.assertEqual(10000, res['status']['code'])
