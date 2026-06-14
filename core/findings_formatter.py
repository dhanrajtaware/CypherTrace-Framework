class FindingsFormatter:

    def format(
        self,
        findings
    ):

        output = []

        for finding in findings:

            module = finding.get(
                "module",
                "Unknown"
            )

            output.append(
                "\n" + "=" * 60
            )

            output.append(
                module.upper()
            )

            output.append(
                "=" * 60
            )

            for key, value in (
                finding.items()
            ):

                if key == "module":
                    continue

                if isinstance(
                    value,
                    dict
                ):

                    output.append(
                        f"\n{key.upper()}:"
                    )

                    for subkey, subvalue in (
                        value.items()
                    ):

                        output.append(
                            f"\n  {subkey}:"
                        )

                        if isinstance(
                            subvalue,
                            list
                        ):

                            for item in subvalue:

                                output.append(
                                    f"    - {item}"
                                )

                        else:

                            output.append(
                                f"    {subvalue}"
                            )

                elif isinstance(
                    value,
                    list
                ):

                    output.append(
                        f"\n{key.upper()}:"
                    )

                    for item in value:

                        output.append(
                            f"  - {item}"
                        )

                else:

                    output.append(
                        f"{key}: {value}"
                    )

            output.append("")

        return "\n".join(
            output
        )