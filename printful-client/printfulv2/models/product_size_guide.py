from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.size_table import SizeTable


T = TypeVar("T", bound="ProductSizeGuide")


@_attrs_define
class ProductSizeGuide:
    r"""Size Guide information for the Product

    Attributes:
        catalog_product_id (int): Product ID Example: 13.
        available_sizes (list[str]): The sizes available for the Product Example: ['S', 'M', 'L'].
        size_tables (list['SizeTable']): Size tables for the product Example: [{'type': 'measure_yourself', 'unit':
            'inches', 'description': '<p>Measurements are provided by suppliers.<br /><br />US customers should order a size
            up as the EU sizes for this supplier correspond to a smaller size in the US market.</p>\\n<p>Product
            measurements may vary by up to 2\\" (5 cm).&nbsp;</p>', 'image_url':
            'https://s3-printful.stage.printful.dev/upload/measure-
            yourself/6a/6a4fe322f592f2b91d5a735d7ff8d1c0_t?v=1652962720', 'image_description': '<h6><strong>A
            Length</strong></h6>\\n<p dir=\\"ltr\\"><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">Place the end of the tape beside the collar at the top of the tee
            (Highest Point Shoulder). Pull the tape measure t</span><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">o the bottom of the shirt.</span></p>\\n<h6>B Chest</h6>\\n<p
            dir=\\"ltr\\">Measure yourself around the fullest part of your chest. Keep the tape measure horizontal.</p>',
            'measurements': [{'type_label': 'Length', 'values': [{'size': 'S', 'value': '24'}, {'size': 'M', 'value': '26'},
            {'size': 'L', 'value': '28'}]}, {'type_label': 'Chest', 'values': [{'size': 'S', 'min_value': '14', 'max_value':
            '16'}, {'size': 'M', 'min_value': '18', 'max_value': '20'}, {'size': 'L', 'min_value': '22', 'max_value':
            '24'}]}]}, {'type': 'product_measure', 'unit': 'inches', 'description': '<p dir=\\"ltr\\">Measurements are
            provided by our suppliers. Product measurements may vary by up to 2\\" (5 cm).</p>\\n<p dir=\\"ltr\\">US
            customers should order a size up as the EU sizes for this supplier correspond to a smaller size in the US
            market.</p>\\n<p dir=\\"ltr\\">Pro tip! Measure one of your products at home and compare with the measurements
            you see in this guide.</p>', 'image_url': 'https://s3-printful.stage.printful.dev/upload/product-
            measure/85/857e7cc8b802da216e7f1a6114075a72_t?v=1652962720', 'image_description': '<h6><strong>A
            Length</strong></h6>\\n<p dir=\\"ltr\\"><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">Place the end of the tape beside the collar at the top of the tee
            (Highest Point Shoulder). Pull the tape measure t</span><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">o the bottom of the shirt.</span></p>\\n<h6>B Width</h6>\\n<p
            dir=\\"ltr\\">Place the end of the tape at the seam under the sleeve and pull the tape measure across the shirt
            to the seam under the opposite sleeve.</p>', 'measurements': [{'type_label': 'Length', 'values': [{'size': 'S',
            'value': '24'}, {'size': 'M', 'value': '26'}, {'size': 'L', 'value': '28'}]}, {'type_label': 'Width', 'values':
            [{'size': 'S', 'min_value': '14', 'max_value': '16'}, {'size': 'M', 'min_value': '18', 'max_value': '20'},
            {'size': 'L', 'min_value': '22', 'max_value': '24'}]}]}, {'type': 'measure_yourself', 'unit': 'cm',
            'description': '<p>Measurements are provided by suppliers.<br /><br />US customers should order a size up as the
            EU sizes for this supplier correspond to a smaller size in the US market.</p>\\n<p>Product measurements may vary
            by up to 2\\" (5 cm).&nbsp;</p>', 'image_url': 'https://s3-printful.stage.printful.dev/upload/measure-
            yourself/6a/6a4fe322f592f2b91d5a735d7ff8d1c0_t?v=1652962720', 'image_description': '<h6><strong>A
            Length</strong></h6>\\n<p dir=\\"ltr\\"><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">Place the end of the tape beside the collar at the top of the tee
            (Highest Point Shoulder). Pull the tape measure t</span><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">o the bottom of the shirt.</span></p>\\n<h6>B Chest</h6>\\n<p
            dir=\\"ltr\\">Measure yourself around the fullest part of your chest. Keep the tape measure horizontal.</p>',
            'measurements': [{'type_label': 'Length', 'values': [{'size': 'S', 'value': '60.96'}, {'size': 'M', 'value':
            '66.04'}, {'size': 'L', 'value': '71.12'}]}, {'type_label': 'Chest', 'values': [{'size': 'S', 'min_value':
            '35.56', 'max_value': '40.64'}, {'size': 'M', 'min_value': '45.72', 'max_value': '50.80'}, {'size': 'L',
            'min_value': '55.88', 'max_value': '60.96'}]}]}, {'type': 'product_measure', 'unit': 'cm', 'description': '<p
            dir=\\"ltr\\">Measurements are provided by our suppliers. Product measurements may vary by up to 2\\" (5
            cm).</p>\\n<p dir=\\"ltr\\">US customers should order a size up as the EU sizes for this supplier correspond to
            a smaller size in the US market.</p>\\n<p dir=\\"ltr\\">Pro tip! Measure one of your products at home and
            compare with the measurements you see in this guide.</p>', 'image_url':
            'https://s3-printful.stage.printful.dev/upload/product-
            measure/85/857e7cc8b802da216e7f1a6114075a72_t?v=1652962720', 'image_description': '<h6><strong>A
            Length</strong></h6>\\n<p dir=\\"ltr\\"><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">Place the end of the tape beside the collar at the top of the tee
            (Highest Point Shoulder). Pull the tape measure t</span><span id=\\"docs-internal-
            guid-a3ac3082-7fff-5f98-2623-3eb38d5f43a1\\">o the bottom of the shirt.</span></p>\\n<h6>B Width</h6>\\n<p
            dir=\\"ltr\\">Place the end of the tape at the seam under the sleeve and pull the tape measure across the shirt
            to the seam under the opposite sleeve.</p>', 'measurements': [{'type_label': 'Length', 'values': [{'size': 'S',
            'value': '60.96'}, {'size': 'M', 'value': '66.04'}, {'size': 'L', 'value': '71.12'}]}, {'type_label': 'Width',
            'values': [{'size': 'S', 'min_value': '35.56', 'max_value': '40.64'}, {'size': 'M', 'min_value': '45.72',
            'max_value': '50.80'}, {'size': 'L', 'min_value': '55.88', 'max_value': '60.96'}]}]}, {'type': 'international',
            'unit': 'none', 'measurements': [{'type_label': 'US size', 'values': [{'size': 'S', 'min_value': '8',
            'max_value': '10'}, {'size': 'M', 'min_value': '12', 'max_value': '14'}, {'size': 'L', 'min_value': '16',
            'max_value': '18'}]}, {'type_label': 'EU size', 'values': [{'size': 'S', 'min_value': '38', 'max_value': '39'},
            {'size': 'M', 'min_value': '40', 'max_value': '41'}, {'size': 'L', 'min_value': '42', 'max_value': '43'}]},
            {'type_label': 'UK size', 'values': [{'size': 'S', 'min_value': '4', 'max_value': '6'}, {'size': 'M',
            'min_value': '8', 'max_value': '10'}, {'size': 'L', 'min_value': '12', 'max_value': '14'}]}]}].
    """

    catalog_product_id: int
    available_sizes: list[str]
    size_tables: list["SizeTable"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_product_id = self.catalog_product_id

        available_sizes = self.available_sizes

        size_tables = []
        for size_tables_item_data in self.size_tables:
            size_tables_item = size_tables_item_data.to_dict()
            size_tables.append(size_tables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_product_id": catalog_product_id,
                "available_sizes": available_sizes,
                "size_tables": size_tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.size_table import SizeTable

        d = dict(src_dict)
        catalog_product_id = d.pop("catalog_product_id")

        available_sizes = cast(list[str], d.pop("available_sizes"))

        size_tables = []
        _size_tables = d.pop("size_tables")
        for size_tables_item_data in _size_tables:
            size_tables_item = SizeTable.from_dict(size_tables_item_data)

            size_tables.append(size_tables_item)

        product_size_guide = cls(
            catalog_product_id=catalog_product_id,
            available_sizes=available_sizes,
            size_tables=size_tables,
        )

        product_size_guide.additional_properties = d
        return product_size_guide

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
