import unittest
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest.mock import MagicMock, patch

from handsdown.md_document import MDDocument


class TestMDDocument(unittest.TestCase):
    def test_init(self):
        with NamedTemporaryFile(mode="w+") as temp_f:
            temp_f.write(
                "\n".join(
                    [
                        "# my title",
                        "",
                        "subtitle",
                        "",
                        "",
                        "",
                        "subtitle2",
                        "",
                        "- [TOC](#toc)",
                        "- [TOC2](#toc2)",
                        "",
                        "## my title 2",
                        "",
                        "some content",
                        "new line",
                    ]
                )
            )
            temp_f.flush()
            md_doc = MDDocument(Path(temp_f.name))
            md_doc.read()

        self.assertEqual(md_doc.path, Path(temp_f.name))
        self.assertEqual(md_doc.title, "my title")
        self.assertEqual(md_doc.subtitle, "subtitle\n\nsubtitle2")
        self.assertEqual(md_doc.toc_section, "- [TOC](#toc)\n- [TOC2](#toc2)")
        self.assertEqual(md_doc.sections[0], "## my title 2")
        self.assertEqual(md_doc.sections[1], "some content\nnew line")

        md_doc.subtitle = "my subtitle"
        self.assertEqual(md_doc.subtitle, "my subtitle")

        with NamedTemporaryFile(mode="w+") as temp_f:
            temp_f.write(
                "\n".join(
                    [
                        "# my title",
                        "",
                        "- [TOC](#toc)",
                        "- [TOC2](#toc2)",
                        "",
                        "",
                        "some content",
                    ]
                )
            )
            temp_f.flush()
            md_doc = MDDocument(Path(temp_f.name))
            md_doc.read()

        self.assertEqual(md_doc.subtitle, "some content")

    def test_context_manager(self):
        with NamedTemporaryFile(mode="w+") as temp_f:
            with MDDocument(Path(temp_f.name)) as md_doc:
                md_doc.title = "test"

            self.assertEqual(temp_f.read(), "# test\n")

        with self.assertRaises(ValueError):
            with MDDocument(Path(temp_f.name)):
                raise ValueError("test")

    def test_add_toc_if_not_exists(self):
        with NamedTemporaryFile(mode="w+") as temp_f:
            temp_f.write(
                "\n".join(
                    [
                        "# header",
                        "",
                        "- [TOC](#toc)",
                        "- [TOC2](#toc2)",
                        "",
                        "## header2",
                        "",
                        "### header3",
                        "",
                    ]
                )
            )
            temp_f.flush()
            md_doc = MDDocument(Path(temp_f.name))
            md_doc.read()
        # md_doc.append_title('header', level=1)
        # md_doc.append_title('header2', level=2)
        self.assertEqual(md_doc.toc_section, "- [TOC](#toc)\n- [TOC2](#toc2)")
        md_doc.add_toc_if_not_exists()
        self.assertEqual(md_doc.toc_section, "- [TOC](#toc)\n- [TOC2](#toc2)")
        md_doc.toc_section = ""
        md_doc.add_toc_if_not_exists()
        self.assertEqual(
            md_doc.toc_section,
            "- [header](#header)\n    - [header2](#header2)\n        - [header3](#header3)",
        )

    def test_append(self):
        md_doc = MDDocument(Path("/test.md"))
        md_doc.append("subtitle")
        md_doc.append("test")
        md_doc.append("")
        self.assertEqual(md_doc.subtitle, "subtitle")
        self.assertEqual(md_doc.sections[0], "test")

    def test_get_anchor(self):
        self.assertEqual(MDDocument.get_anchor("s T_e-s%t"), "s-t_e-st")
        self.assertEqual(MDDocument.get_anchor("test"), "test")

    @patch("handsdown.md_document.MDDocument.render_doc_link")
    def test_render_md_doc_link(self, render_doc_link_mock):
        md_doc_mock = MagicMock()
        md_doc_mock.title = "Other title"
        md_doc_mock.path = "other/test.md"
        render_doc_link_mock.return_value = "result"
        md_doc = MDDocument(Path("/root/test.md"))

        self.assertEqual(md_doc.render_md_doc_link(md_doc_mock), "result")
        render_doc_link_mock.assert_called_with(
            anchor="other-title", target_path="other/test.md", title="Other title"
        )

        self.assertEqual(md_doc.render_md_doc_link(md_doc_mock, title="Test"), "result")
        render_doc_link_mock.assert_called_with(
            anchor="other-title", target_path="other/test.md", title="Test"
        )

    def test_render_doc_link(self):
        md_doc = MDDocument(Path("/root/test.md"))
        self.assertEqual(md_doc.render_doc_link("title", anchor="tag"), "[title](#tag)")
        self.assertEqual(
            md_doc.render_doc_link("title", anchor="tag", target_path=Path("/root/test.md")),
            "[title](#tag)",
        )
        self.assertEqual(
            md_doc.render_doc_link("title", anchor="tag", target_path=Path("/root/test2.md")),
            "[title](test2.md#tag)",
        )
        self.assertEqual(
            md_doc.render_doc_link("title", target_path=Path("/root/test.md")),
            "[title]()",
        )
        self.assertEqual(
            md_doc.render_doc_link("title", target_path=Path("/root/test2.md")),
            "[title](test2.md)",
        )
        self.assertEqual(md_doc.render_doc_link("title"), "[title]()")

    def test_render_link(self):
        self.assertEqual(MDDocument.render_link("title", link="#tag"), "[title](#tag)")
        self.assertEqual(MDDocument.render_link("title", link=""), "[title]()")

    def test_is_toc(self):
        self.assertTrue(MDDocument.is_toc("- [TOC](#toc)\n- [TOC2](#toc2)"))
        self.assertFalse(MDDocument.is_toc("- [TOC](#toc)\n- [TOC2](#toc2)\nTOC3"))
        self.assertFalse(MDDocument.is_toc("- [TOC](#toc)\n"))
